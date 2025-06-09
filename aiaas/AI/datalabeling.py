import cv2
import numpy as np
import matplotlib.pyplot as plt


def create_detection_dataset():
    """객체 검출용 바운딩 박스 라벨링 예제"""
    plt.rc('font', family='Malgun Gothic')

    def create_multi_object_image():
        """여러 객체가 있는 이미지 생성"""
        image = np.zeros((200, 300, 3), dtype=np.uint8)
        bboxes = []
        class_ids = []

        num_objects = np.random.randint(1, 4)

        for _ in range(num_objects):
            obj_type = np.random.choice(['circle', 'rectangle'])

            x = np.random.randint(20, 280)
            y = np.random.randint(20, 180)
            size = np.random.randint(15, 35)

            if obj_type == 'circle':
                cv2.circle(image, (x, y), size, (255, 255, 255), -1)
                bbox = [x-size, y-size, x+size, y+size]
                class_id = 0
            else:
                cv2.rectangle(image, (x-size, y-size), (x+size, y+size), (255, 255, 255), -1)
                bbox = [x-size, y-size, x+size, y+size]
                class_id = 1

            bboxes.append(bbox)
            class_ids.append(class_id)

        return image, bboxes, class_ids

    detection_images = []
    detection_bboxes = []
    detection_classes = []

    for i in range(6):
        img, bboxes, class_ids = create_multi_object_image()
        detection_images.append(img)
        detection_bboxes.append(bboxes)
        detection_classes.append(class_ids)

    plt.figure(figsize=(18, 12))

    for i in range(6):
        plt.subplot(2, 3, i+1)
        img_with_boxes = detection_images[i].copy()

        for bbox, class_id in zip(detection_bboxes[i], detection_classes[i]):
            x_min, y_min, x_max, y_max = bbox
            color = (255, 0, 0) if class_id == 0 else (0, 255, 0)
            cv2.rectangle(img_with_boxes, (x_min, y_min), (x_max, y_max), color, 2)

            label = 'Circle' if class_id == 0 else 'Rectangle'
            cv2.putText(img_with_boxes, label, (x_min, y_min-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

        plt.imshow(cv2.cvtColor(img_with_boxes, cv2.COLOR_BGR2RGB))
        plt.title(f'이미지 {i+1}: {len(detection_bboxes[i])}개 객체')
        plt.axis('off')

    plt.tight_layout()
    plt.show()

    return detection_images, detection_bboxes, detection_classes


det_images, det_bboxes, det_classes = create_detection_dataset()
