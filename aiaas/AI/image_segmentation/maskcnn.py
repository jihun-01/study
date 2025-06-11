import torch
from torchvision.models.detection import maskrcnn_resnet50_fpn
from torchvision.transforms import functional as F
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from PIL import Image

class MaskRCNNPredictor:

    def __init__(self, device='cuda' if torch.cuda.is_available() else 'cpu'):

        self.device = device
        self.model = maskrcnn_resnet50_fpn(pretrained=True)
        self.model.to(device)
        self.model.eval()

        self.class_names = [
            '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
            'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 'stop sign',
            'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
            'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A',
            'N/A', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard',
            'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard',
            'surfboard', 'tennis racket', 'bottle', 'N/A', 'wine glass', 'cup', 'fork',
            'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange',
            'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
            'potted plant', 'bed', 'N/A', 'dining table', 'N/A', 'N/A', 'toilet',
            'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
            'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A', 'book',
            'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
        ]      

    def predict(self, image_path, confidence_threshold=0.5):

        image = Image.open(image_path).convert('RGB')

        image_tensor = F.to_tensor(image).unsqueeze(0).to(self.device)

        with torch.no_grad():
            predictions = self.model(image_tensor)

        pred = predictions[0]

        keep_idx = pred['scores'] > confidence_threshold

        boxes = pred['boxes'][keep_idx].cpu().numpy()
        labels = pred['labels'][keep_idx].cpu().numpy()
        scores = pred['scores'][keep_idx].cpu().numpy()
        masks = pred['masks'][keep_idx].cpu().numpy()

        return image, boxes, labels, scores, masks
    
    def visualize_results(self, image, boxes, labels, scores, masks):

        fig,axes = plt.subplots(1, 2, figsize=(15, 7))

        axes[0].imshow(image)
        axes[0].set_title('Object Detection')
        axes[0].axis('off')

        for i, (box, label, score) in enumerate(zip(boxes, labels, scores)):
            x1, y1, x2, y2 = box
            rect = patches.Rectangle((x1, y1), x2 - x1, y2 - y1,
                                      linewidth=2, edgecolor='red', facecolor='none')
            
            axes[0].add_patch(rect)

            class_name = self.class_names[label]
            axes[0].text(x1, y1, f'{class_name}: {score:.2f}',
                         color='red', fontsize=10, weight='bold')

        colors = plt.cm.Set1(np.linspace(0, 1, len(masks)))

        for i, mask in enumerate(masks):
            mask_colored = np.zeros((*mask.shape[1:], 4))

            mask_colored[:, :, :3] = colors[i][:3]
            mask_colored[:, :, 3] = mask[0] * 0.7
            axes[1].imshow(mask_colored)

        plt.tight_layout()
        plt.show()


def demo_maskrcnn():

    predictor = MaskRCNNPredictor()
    image, boxes, labels, scores, masks = predictor.predict('testimage.png')
    predictor.visualize_results(image, boxes, labels, scores, masks)

    print("Mask R-CNN 모델이 준비되었습니다.")
    print(f"지원하는 클래스 수: {len(predictor.class_names)}")
    print(f"사용 디바이스: {predictor.device}")

    print("\n지원하는 주요 클래스들:")
    for i, class_name in enumerate(predictor.class_names[1:21]):
        print(f"  {i+1}: {class_name}")

demo_maskrcnn()



