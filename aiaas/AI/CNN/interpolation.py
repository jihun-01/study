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

def demonstrate_resize_methods():

    original = create_sample_image()
    print(f"원본 이미지 크기: {original.shape}")

    interpolations = {
        'NEAREST': cv2.INTER_NEAREST,
        'LINEAR': cv2.INTER_LINEAR,
        'CUBIC': cv2.INTER_CUBIC,
        'LANCZOS': cv2.INTER_LANCZOS4
    }

    target_sizes = (200,150)

    plt.subplot(2, 3, 1)
    plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    plt.title(f'원본\n {original.shape[1]}x{original.shape[0]}')
    plt.axis('off')

    for i, (name, method) in enumerate(interpolations.items()):
        resized = cv2.resize(original, target_sizes, interpolation=method)

        plt.subplot(2, 3, i+2)
        plt.imshow(cv2.cvtColor(resized, cv2.COLOR_BGR2RGB))
        plt.title(f'{name}\n {target_sizes[0]}x{target_sizes[1]}')
        plt.axis('off')

    plt.tight_layout()
    plt.show()

def resize_keep_ratio(image, max_size=300):
    height, width = image.shape[:2]

    if max(height, width) > max_size:
        if height > width:
            new_height = max_size
            new_width = int(width * max_size / height)
        else:
            new_width = max_size
            new_height = int(height * max_size / width)

    else:
        new_height, new_width = height, width

    resized = cv2.resize(image, (new_width, new_height))
    return resized

original = create_sample_image()

resized_ratio = resize_keep_ratio(original, 200)

plt.figure(figsize=(12, 6))
plt.rc('font', family='Malgun Gothic')
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
plt.title(f'원본: {original.shape[1]}x{original.shape[0]}')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(resized_ratio, cv2.COLOR_BGR2RGB))
plt.title(f'비율 유지 크기: {resized_ratio.shape[1]}x{resized_ratio.shape[0]}')
plt.axis('off')

plt.show()

demonstrate_resize_methods()

