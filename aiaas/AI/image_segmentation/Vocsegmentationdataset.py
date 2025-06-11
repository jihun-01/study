import torch
import torchvision
from torch.utils.data import DataLoader
import torchvision.transforms as transforms
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


class VOCSegmentationDataset():

    def __init__(self, root='./data', train=True, download=True):

        
        self.transforms = transforms.Compose([
            transforms.Resize((256, 256)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])

        
        self.target_transforms = transforms.Compose([
            transforms.Resize((256, 256), interpolation=Image.NEAREST),
            transforms.ToTensor(),
        ])

        self.dataset = torchvision.datasets.VOCSegmentation(
            root=root,
            year='2012',
            image_set='train' if train else 'val',
            download=download,
            transform=self.transforms,
            target_transform=self.target_transforms,
        )

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):

        return self.dataset[idx]
    
    def get_class_names(self):
        return [
            'background','aeroplane','bicycle','bird','boat',
            'bottle','bus','car','cat','chair','cow',
            'diningtable','dog','horse','motorbike','person',
            'pottedplant','sheep','sofa','train','tvmonitor'
        ]
    
    def visualize_segmentation_data():
        dataset = VOCSegmentationDataset(train=True, download=True)
        dataloader = DataLoader(dataset, batch_size=4, shuffle=True)
        images, targets = next(iter(dataloader))
        fig, axes = plt.subplots(2, 4, figsize=(16, 8))

        for i in range(4):
            img = images[i]
            img = img * torch.tensor([0.229, 0.224, 0.225]).view(3, 1, 1)
            img = img + torch.tensor([0.485, 0.456, 0.406]).view(3, 1, 1)
            img = torch.clamp(img, 0, 1)
            img = img.permute(1, 2, 0)
            target = targets[i].squeeze().numpy()

            axes[0, i].imshow(img)
            axes[0, i].set_title(f'Original Image {i+1}')
            axes[0, i].axis('off')

            axes[1, i].imshow(target)
            axes[1, i].set_title(f'Segmentation Mask {i+1}')
            axes[1, i].axis('off')

        plt.tight_layout()
        plt.show()

VOCSegmentationDataset.visualize_segmentation_data()