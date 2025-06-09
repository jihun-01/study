import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as transforms
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import string
import random

class CRNN(nn.Module):
    def __init__(self, img_height, img_width, num_chars, num_classes, rnn_hidden=256):
        super().__init__()
        self.img_height = img_height
        self.img_width = img_width
        self.num_chars = num_chars
        self.num_classes = num_classes
        self.cnn = nn.Sequential(
            nn.Conv2d(1, 64, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(128, 256, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, 256, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True),
            nn.MaxPool2d((2, 1)),
            nn.Conv2d(256, 512, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(512),
            nn.ReLU(inplace=True),
            nn.Conv2d(512, 512, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(512),
            nn.ReLU(inplace=True),
            nn.MaxPool2d((2, 1)),
            nn.Conv2d(512, 512, 2, 1, 0),
            nn.ReLU()
        )
        self.rnn = nn.LSTM(512, rnn_hidden, bidirectional=True, batch_first=True)
        self.linear = nn.Linear(rnn_hidden * 2, num_classes)

    def forward(self, x):
        conv_features = self.cnn(x)
        b, c, h, w = conv_features.size()
        conv_features = conv_features.view(b, c * h, w)
        conv_features = conv_features.permute(0, 2, 1)
        rnn_out, _ = self.rnn(conv_features)
        output = self.linear(rnn_out)
        output = F.log_softmax(output, dim=2)
        return output

class SyntheticTextDataset(Dataset):
    def __init__(self, num_samples=1000, img_height=32, img_width=128, max_text_len=6):
        self.num_samples = num_samples
        self.img_height = img_height
        self.img_width = img_width
        self.max_text_len = max_text_len
        self.chars = string.digits
        self.char_to_idx = {char: idx+1 for idx, char in enumerate(self.chars)}
        self.char_to_idx['<blank>'] = 0
        self.idx_to_char = {idx: char for char, idx in self.char_to_idx.items()}
        self.num_classes = len(self.chars) + 1
        self.transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.5,), (0.5,))
        ])

    def __len__(self):
        return self.num_samples

    def __getitem__(self, idx):
        text_len = random.randint(2, min(4, self.max_text_len))
        text = ''.join(random.choices(self.chars, k=text_len))
        image = self.create_text_image(text)
        label = [self.char_to_idx[char] for char in text]
        if self.transform:
            image = self.transform(image)
        return image, torch.tensor(label, dtype=torch.long), text

    def create_text_image(self, text):
        img = Image.new('L', (self.img_width, self.img_height), 255)
        draw = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype("arial.ttf", 24)
        except:
            font = ImageFont.load_default()
        try:
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
        except AttributeError:
            text_width, text_height = draw.textsize(text, font=font)
        x = (self.img_width - text_width) // 2
        y = (self.img_height - text_height) // 2
        draw.text((x, y), text, fill=0, font=font)
        img_array = np.array(img)
        noise = np.random.normal(0, 5, img_array.shape)
        img_array = np.clip(img_array + noise, 0, 255).astype(np.uint8)
        return Image.fromarray(img_array)

class CRNNTrainer:
    def __init__(self, model, device='cpu'):
        self.model = model.to(device)
        self.device = device
        self.criterion = nn.CTCLoss(blank=0, reduction='mean', zero_infinity=True)
        self.optimizer = optim.Adam(model.parameters(), lr=0.0005, weight_decay=1e-4)
        self.scheduler = optim.lr_scheduler.StepLR(self.optimizer, step_size=3, gamma=0.5)

    def train_epoch(self, dataloader):
        self.model.train()
        total_loss = 0
        num_batches = 0
        for batch_idx, (images, targets, texts) in enumerate(dataloader):
            images = images.to(self.device)
            targets = [target.to(self.device) for target in targets]
            outputs = self.model(images)
            outputs = outputs.permute(1, 0, 2)
            input_lengths = torch.full((images.size(0),), outputs.size(0), dtype=torch.long)
            target_lengths = torch.tensor([len(target) for target in targets], dtype=torch.long)
            targets_1d = torch.cat(targets)
            loss = self.criterion(outputs, targets_1d, input_lengths, target_lengths)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(self.model.parameters(), max_norm=1.0)
            self.optimizer.step()
            total_loss += loss.item()
            num_batches += 1
            if batch_idx % 50 == 0:
                print(f'Batch {batch_idx}, Loss: {loss.item():.4f}')
        self.scheduler.step()
        return total_loss / num_batches

    def decode_prediction(self, output, dataset):
        pred_indices = torch.argmax(output, dim=2)
        decoded_texts = []
        for batch_idx in range(pred_indices.size(0)):
            indices = pred_indices[batch_idx].cpu().numpy()
            decoded_chars = []
            prev_idx = -1
            for idx in indices:
                if idx != 0 and idx != prev_idx:
                    if idx in dataset.idx_to_char:
                        decoded_chars.append(dataset.idx_to_char[idx])
                prev_idx = idx
            decoded_texts.append(''.join(decoded_chars))
        return decoded_texts

    def evaluate(self, dataloader, dataset, num_samples=10):
        self.model.eval()
        correct = 0
        total = 0
        with torch.no_grad():
            for batch_idx, (images, targets, gt_texts) in enumerate(dataloader):
                if batch_idx >= num_samples:
                    break
                images = images.to(self.device)
                outputs = self.model(images)
                predicted_texts = self.decode_prediction(outputs, dataset)
                for pred, gt in zip(predicted_texts, gt_texts):
                    if pred == gt:
                        correct += 1
                    total += 1
                    print(f"GT: '{gt}' | Pred: '{pred}' | {'✓' if pred == gt else 'X'}")
        accuracy = correct / total if total > 0 else 0
        print(f"\nAccuracy: {accuracy:.4f} ({correct}/{total})")
        return accuracy

def crnn_practice():
    print("=== CRNN OCR 실습 ===\n")
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"사용 디바이스: {device}")
    print("\n1. 합성 데이터셋 생성")
    train_dataset = SyntheticTextDataset(num_samples=1000, img_height=32, img_width=128)
    test_dataset = SyntheticTextDataset(num_samples=100, img_height=32, img_width=128)
    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True, collate_fn=collate_fn)
    test_loader = DataLoader(test_dataset, batch_size=16, shuffle=False, collate_fn=collate_fn)
    print(f"훈련 데이터: {len(train_dataset)}개, 테스트 데이터: {len(test_dataset)}개")
    print(f"문자 집합: {train_dataset.chars}")
    sample_image, sample_label, sample_text = train_dataset[0]
    plt.rc('font', family='Malgun Gothic')
    plt.figure(figsize=(10, 3))
    plt.imshow(sample_image.squeeze(), cmap='gray')
    plt.title(f"샘플 이미지: '{sample_text}'")
    plt.axis('off')
    plt.show()
    print("\n2. CRNN 모델 생성")
    model = CRNN(
        img_height=32,
        img_width=128,
        num_chars=len(train_dataset.chars),
        num_classes=train_dataset.num_classes
    )
    print(f"모델 파라미터 수: {sum(p.numel() for p in model.parameters()):,}")
    print("\n3. 모델 훈련")
    trainer = CRNNTrainer(model, device)
    num_epochs = 30
    for epoch in range(num_epochs):
        print(f"\nEpoch {epoch+1}/{num_epochs}")
        avg_loss = trainer.train_epoch(train_loader)
        current_lr = trainer.optimizer.param_groups[0]['lr']
        print(f"평균 손실: {avg_loss:.4f}, 학습률: {current_lr:.6f}")
        if (epoch + 1) % 2 == 0:
            print(f"\n{epoch+1} 에포크 평가:")
            trainer.evaluate(test_loader, test_dataset, num_samples=5)
    print("\n4. 최종 평가")
    final_accuracy = trainer.evaluate(test_loader, test_dataset, num_samples=20)
    return model, train_dataset, test_dataset

def collate_fn(batch):
    images, labels, texts = zip(*batch)
    images = torch.stack(images)
    labels = list(labels)
    return images, labels, texts

# 실행
model, train_dataset, test_dataset = crnn_practice()

