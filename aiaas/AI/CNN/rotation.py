import cv2
import numpy as np
import matplotlib.pyplot as plt



def create_sample_image():
    width, height = 400, 300
    image = np.zeros((height, width, 3), dtype=np.uint8)
    cv2.rectangle(image, (50,50), (150,150), (255,255,255), -1)
    cv2.circle(image, (300,200), 50, (0,255,255), -1)
    cv2.line(image, (200,100), (350,250), (255,0,255),3)
    return image

def rotate_image_example():

    original = create_sample_image()
    height, width = original.shape[:2]
    center = (width // 2, height // 2)

    angles = [0, 45, 90, 135, 180, 270]

    plt.figure(figsize=(18, 6))

    for i, angle in enumerate(angles):
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(original, rotation_matrix, (width, height))

        plt.subplot(2, 3, i+1)
        plt.imshow(cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB))
        plt.title(f'{angle}도 회전')
        plt.axis('off')

    plt.tight_layout()
    plt.show()


def rotate_without_crop(image, angle):
    height, width = image.shape[:2]
    center = (width // 2, height // 2)

    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    cos_val = np.abs(rotation_matrix[0, 0])
    sin_val = np.abs(rotation_matrix[0, 1])

    new_width = int((height * sin_val) + (width * cos_val))
    new_height = int((height * cos_val) + (width * sin_val))

    rotation_matrix[0, 2] += (new_width / 2 ) - center[0]
    rotation_matrix[1, 2] += (new_height / 2 ) - center[1]

    rotated = cv2.warpAffine(image, rotation_matrix, (new_width, new_height))
    return rotated


original = create_sample_image()
angle = 45

# 일반 회전 (잘림)
normal_rotated = cv2.warpAffine(
    original,
    cv2.getRotationMatrix2D((original.shape[1] // 2, original.shape[0] // 2), angle, 1.0),
    (original.shape[1], original.shape[0])
)

# 잘림 없는 회전
no_crop_rotated = rotate_without_crop(original, angle)
plt.rc('font', family='Malgun Gothic')

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
plt.title('원본')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(normal_rotated, cv2.COLOR_BGR2RGB))
plt.title('일반 회전 (잘림)')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(no_crop_rotated, cv2.COLOR_BGR2RGB))
plt.title('잘림 없는 회전')
plt.axis('off')

plt.tight_layout()
plt.show()


rotate_image_example()
