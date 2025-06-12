import torch
from transformers import BertTokenizer, BertForSequenceClassification
import pandas as pd
from sklearn.preprocessing import LabelEncoder

class IntentClassifier:

    def __init__(self, model_name='klue/bert-base'):
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = None
        self.label_encoder = LabelEncoder()

    def prepare_data(self,texts,labels):

        encoded_labels = self.label_encoder.fit_transform(labels)
        encodings = self.tokenizer(
            texts,
            truncation=True,
            padding=True,
            max_length=128,
            return_tensors='pt'
        )
        print(f"encodings: {encodings}")
        print(f"encoded_labels: {encoded_labels}")
        return encodings, encoded_labels
    
    def train(self, train_texts, train_labels):
        num_labels = len(set(train_labels))
        self.model = BertForSequenceClassification.from_pretrained(
            'klue/bert-base',
            num_labels=num_labels,
        )

        train_encodings, train_labels = self.prepare_data(train_texts, train_labels)

        class IntentDataset(torch.utils.data.Dataset):
            def __init__(self, encodings, labels):
                self.encodings = encodings
                self.labels = labels

            def __getitem__(self, idx):
                item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
                item['labels'] = torch.tensor(self.labels[idx])
                return item
            
            def __len__(self):
                return len(self.labels)
        
        train_dataset = IntentDataset(train_encodings,train_labels)
        
        batch_size = 16
        epochs = 10
        learning_rate = 2e-5
        weight_decay = 0.01

        train_dataloader = torch.utils.data.DataLoader(
            train_dataset, 
            batch_size=batch_size, 
            shuffle=True
        )

        optimizer = torch.optim.AdamW(
            self.model.parameters(),
            lr=learning_rate,
            weight_decay=weight_decay
        )

        self.model.train()

        for epoch in range(epochs):
            print(f"Epoch {epoch+1}/{epochs}")
            total_loss = 0

            for batch in train_dataloader:
                optimizer.zero_grad()

                outputs = self.model(**batch)
                loss = outputs.loss

                loss.backward()

                torch.nn.utils.clip_grad_norm_(self.model.parameters(),1.0)

                optimizer.step()

                total_loss += loss.item()
            
            avg_loss = total_loss / len(train_dataloader)
            print(f"Average loss: {avg_loss:.4f}")
        
        print("훈련완료")

    def predict(self, text):

        inputs = self.tokenizer(text, return_tensors='pt', padding=True, truncation=True)


        with torch.no_grad():
            outputs = self.model(**inputs)
            predictions = torch.nn.functional.softmax(outputs.logits, dim=1)
        
        predicted_class = torch.argmax(predictions, dim=1).item()

        confidence = torch.max(predictions, dim=1).values.item()

        intent = self.label_encoder.inverse_transform([predicted_class])[0]

        return intent, confidence
    

if __name__ == '__main__':

    classifier = IntentClassifier()

    train_texts = [
    "안녕하세요", "반갑습니다", "hello",
    "날씨가 어때요?", "비가 와요?", "맑나요?",
    "주문하고 싶어요", "메뉴 보여줘", "배달 가능해?"
    ]   

    train_labels = [
        "greeting", "greeting", "greeting",
        "weather", "weather", "weather",
        "order", "order", "order"
    ]

    classifier.train(train_texts, train_labels)

    intent, confidence = classifier.predict("오늘 날씨 어때요?")

    print(f"의도: {intent}, 신뢰도: {confidence:.2f}")
    
    
