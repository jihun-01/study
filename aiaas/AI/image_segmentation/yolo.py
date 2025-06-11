from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import numpy as np


class YOLOSegmentation:

    def __init__(self, model_name='yolov8n-seg.pt'):
        self.model = YOLO(model_name)

    def predict_and_visualize(self, image_path, confidence=0.5):
        results = self.model(image_path, conf=confidence)

        for r in results:
            img = cv2.imread(image_path)
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            fig, axes = plt.subplots(1, 3, figsize=(18, 6))

            axes[0].imshow(img_rgb)
            axes[0].set_title('Original Image')
            axes[0].axis('off')

            img_with_boxes = r.plot()

            axes[1].imshow(img_with_boxes)
            axes[1].set_title('Detection Results')
            axes[1].axis('off')

            if r.masks is not None:
                masks = r.masks.data.cpu().numpy()
                combined_mask = np.zeros_like(img_rgb)

                for i, mask in enumerate(masks):

                    mask_resized = cv2.resize(mask, (img_rgb.shape[1], img_rgb.shape[0]))

                    color = np.random.randint(0, 255, 3)

                    colored_mask = np.zeros_like(img_rgb)
                    colored_mask[mask_resized > 0.5] = color
                    combined_mask = cv2.addWeighted(combined_mask, 1, colored_mask, 0.7, 0)
                
                result_img = cv2.addWeighted(img_rgb, 0.6, combined_mask, 0.4, 0)
                axes[2].imshow(result_img)
                axes[2].set_title('Segmentation Masks')
            
            else:

                axes[2].text(0.5, 0.5, 'No Masks Detected',
                              transform=axes[2].transAxes, ha='center', va='center')
                axes[2].set_title('No Segmentation Masks')
            axes[2].axis('off')
            plt.tight_layout()
            plt.show()

            if r.boxes is not None:
                print(f"검출된 객체 수: {len(r.boxes)}")

                for i, box in enumerate(r.boxes):
                    class_id = int(box.cls[0])
                    confidence = float(box.conf[0])
                    class_name = self.model.names[class_id]

                    print(f"객체 {i+1}: {class_name} (신뢰도: {confidence:.2f})")

def demo_yolo_segmentation():
    yolo_seg = YOLOSegmentation()
    print("YOLO 세그멘테이션 모델이 준비되었습니다.")
    print(f"지원하는 클래스: {list(yolo_seg.model.names.values())}")

    yolo_seg.predict_and_visualize('testimage.png')

demo_yolo_segmentation()




