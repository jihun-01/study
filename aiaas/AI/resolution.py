import numpy as np
import cv2
import matplotlib.pyplot as plt

original_size = (400,400,3)
original_image = np.random.randint(0,256, original_size, dtype=np.uint8)

resolutions = [(400,400), (200,200), (100,100), (50,50)]

plt.figure(figsize=(16, 4))
for i,(width, height) in enumerate(resolutions):
    resized_image = cv2.resize(original_image, (width, height))
    plt.rc('font', family='Malgun Gothic')
    plt.subplot(1, 4, i+1)
    plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
    plt.title(f'{width}x{height}\n {width*height} 픽셀')
    plt.axis('off')
    file_size = resized_image.nbytes
    print(f"{width}x{height}: {file_size} bytes ({file_size/1024:.1f} KB)")

plt.tight_layout()
plt.show()


def analyze_resolution_quality(image, target_size):
    """해상도 변경이 이미지 품질에 미치는 영향 분석"""
    resized = cv2.resize(image, target_size)
    restored = cv2.resize(resized, (image.shape[1], image.shape[0]))

    mse = np.mean((image.astype(float) - restored.astype(float)) ** 2)

    return resized, restored, mse

test_image = np.random.randint(0, 256, (200, 200, 3), dtype=np.uint8)
sizes = [(100, 100), (50, 50), (25, 25)]

for size in sizes:
    _, restored, mse = analyze_resolution_quality(test_image, size)
    print(f"해상도 {size}: MSE = {mse:.2f}")

