import cv2
import matplotlib.pyplot as plt
import numpy as np

def create_sample_image():
    width, height = 400, 300
    image = np.zeros((height, width, 3), dtype=np.uint8)
    cv2.rectangle(image, (50,50), (150,150), (255,255,255), -1)
    cv2.circle(image, (300,200), 50, (0,255,255), -1)
    cv2.line(image, (200,100), (350,250), (255,0,255),3)
    return image


def medical_image_normalization(image):
    if len(image.shape) == 3:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray_image = image

    denoised = cv2.medianBlur(gray_image, 3)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    enhanced = clahe.apply(denoised)

    normalized = (enhanced - enhanced.min()) / (enhanced.max() - enhanced.min())

    return normalized

image = create_sample_image()
normalized = medical_image_normalization(image)

plt.figure(figsize=(12, 6))
plt.rc('font', family='Malgun Gothic')

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('원본 이미지')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(normalized, cmap='gray')
plt.title('정규화된 이미지')
plt.axis('off')

plt.tight_layout()
plt.show()
