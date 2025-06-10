import cv2
import numpy as np
import matplotlib.pyplot as plt


def create_labeled_dataset():
    def create_shape_image(shape_type, size=(100, 100)):
        image = np.zeros((size[0], size[1], 3), dtype=np.uint8)
        center = (size[1]//2, size[0]//2)

        if shape_type == 'circle':
            cv2.circle(image, center, 30, (255, 255, 255), -1)
            label = 0
        elif shape_type == 'rectangle':
            cv2.rectangle(image, (center[0]-25, center[1]-25),
                          (center[0]+25, center[1]+25), (255, 255, 255), -1)
            label = 1  # 사각형
        elif shape_type == 'triangle':
            points = np.array([[center[0], center[1]-30],
                               [center[0]-26, center[1]+15],
                               [center[0]+26, center[1]+15]], np.int32)
            cv2.fillPoly(image, [points], (255, 255, 255))
            label = 2  # 삼각형

        return image, label

    dataset = []
    labels = []
    class_names = ['원', '사각형', '삼각형']

    for shape_type in ['circle', 'rectangle', 'triangle']:
        for i in range(10):
            img, label = create_shape_image(shape_type)

            if i % 2 == 0:
                noise = np.random.normal(0, 20, img.shape).astype(np.int16)
                img = np.clip(img.astype(np.int16) + noise, 0, 255).astype(np.uint8)

            if i % 3 == 0:
                angle = np.random.uniform(-30, 30)
                M = cv2.getRotationMatrix2D((50, 50), angle, 1.0)
                img = cv2.warpAffine(img, M, (100, 100))

            dataset.append(img)
            labels.append(label)

    dataset = np.array(dataset)
    labels = np.array(labels)

    print(f"데이터셋 형태: {dataset.shape}")
    print(f"라벨 형태: {labels.shape}")
    print(f"클래스별 개수: {np.bincount(labels)}")

    return dataset, labels, class_names

from sklearn.model_selection import train_test_split
from collections import Counter

def demonstrate_data_splitting():
    plt.rc('font', family='Malgun Gothic')
    X, y, class_names = create_labeled_dataset()

    print(f"전체 데이터: {len(X)}개")
    print(f"클래스별 분포: {Counter(y)}")

    X_train, X_temp, y_train, y_temp = train_test_split(
        X, y, test_size=0.4, random_state=42, stratify=y
    )
    X_val, X_test, y_val, y_test = train_test_split(
        X_temp, y_temp, test_size=0.5, random_state=42, stratify=y_temp
    )

    print(f"\n=== 데이터 분할 결과 ===")
    print(f"학습 세트: {len(X_train)}개 ({len(X_train)/len(X)*100:.1f}%)")
    print(f"검증 세트: {len(X_val)}개 ({len(X_val)/len(X)*100:.1f}%)")
    print(f"테스트 세트: {len(X_test)}개 ({len(X_test)/len(X)*100:.1f}%)")

    print(f"\n=== 클래스 분포 ===")
    print(f"학습 세트: {Counter(y_train)}")
    print(f"검증 세트: {Counter(y_val)}")
    print(f"테스트 세트: {Counter(y_test)}")

    plt.figure(figsize=(15, 8))

    sets_data = [
        ('전체', y, X),
        ('학습', y_train, X_train),
        ('검증', y_val, X_val),
        ('테스트', y_test, X_test)
    ]

    for i, (set_name, labels, images) in enumerate(sets_data):
        plt.subplot(2, 4, i+1)

        class_counts = [np.sum(labels == j) for j in range(3)]
        colors = ['red', 'green', 'blue']
        bars = plt.bar(range(3), class_counts, color=colors, alpha=0.7)
        plt.title(f'{set_name} 세트\n총 {len(labels)}개')
        plt.xlabel('클래스')
        plt.ylabel('개수')
        plt.xticks(range(3), class_names)

        for bar, count in zip(bars, class_counts):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                     str(count), ha='center', va='bottom')

        plt.subplot(2, 4, i+5)
        if len(images) > 0:
            sample_indices = []
            for class_id in range(3):
                class_indices = np.where(labels == class_id)[0]
                if len(class_indices) > 0:
                    sample_indices.append(class_indices[0])

            if len(sample_indices) > 0:
                sample_img = images[sample_indices[0]]
                plt.imshow(cv2.cvtColor(sample_img, cv2.COLOR_BGR2RGB))
                plt.title(f'{set_name} 샘플')
            plt.axis('off')

    plt.tight_layout()
    plt.show()

    return X_train, X_val, X_test, y_train, y_val, y_test


split_results = demonstrate_data_splitting()
