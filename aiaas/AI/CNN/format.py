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



def demonstrate_format_conversion():
    """다양한 포맷 변환 시연"""

    original = create_sample_image()
    plt.rc('font', family='Malgun Gothic')

    color_spaces = {
        '원본 (BGR)': original,
        'RGB': cv2.cvtColor(original, cv2.COLOR_BGR2RGB),
        '그레이스케일': cv2.cvtColor(original, cv2.COLOR_BGR2GRAY),
        'HSV': cv2.cvtColor(original, cv2.COLOR_BGR2HSV),
        'LAB': cv2.cvtColor(original, cv2.COLOR_BGR2LAB),
        'YUV': cv2.cvtColor(original, cv2.COLOR_BGR2YUV)
    }

    plt.figure(figsize=(18, 12))

    for i, (name, img) in enumerate(color_spaces.items()):
        plt.subplot(2, 3, i+1)
        
        if len(img.shape) == 2:  # 그레이스케일
            plt.imshow(img, cmap='gray')
        elif name == '원본 (BGR)':
            plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        else:
            plt.imshow(img)

        plt.title(name)
        plt.axis('off')

        print(f"{name}: 형태 {img.shape}, 데이터 타입 {img.dtype}")

    plt.tight_layout()
    plt.show()


def analyze_hsv_channels():
    """HSV 채널별 분석"""

    original = create_sample_image()
    hsv = cv2.cvtColor(original, cv2.COLOR_BGR2HSV)

    h, s, v = cv2.split(hsv)
    plt.rc('font', family='Malgun Gothic')
    plt.figure(figsize=(16, 4))

    plt.subplot(1, 4, 1)
    plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    plt.title('원본')
    plt.axis('off')

    plt.subplot(1, 4, 2)
    plt.imshow(h, cmap='hsv')
    plt.title('Hue (색상)')
    plt.axis('off')

    plt.subplot(1, 4, 3)
    plt.imshow(s, cmap='gray')
    plt.title('Saturation (채도)')
    plt.axis('off')

    plt.subplot(1, 4, 4)
    plt.imshow(v, cmap='gray')
    plt.title('Value (명도)')
    plt.axis('off')

    plt.tight_layout()
    plt.show()


def file_format_operations():
    """파일 포맷 저장/로드 예제"""

    sample = create_sample_image()

    formats = ['jpg', 'png', 'bmp']
    file_sizes = {}

    for fmt in formats:
        filename = f"sample.{fmt}"

        if fmt == 'jpg':
            cv2.imwrite(filename, sample, [cv2.IMWRITE_JPEG_QUALITY, 95])
        elif fmt == 'png':
            cv2.imwrite(filename, sample, [cv2.IMWRITE_PNG_COMPRESSION, 9])
        else:
            cv2.imwrite(filename, sample)

        if fmt == 'jpg':
            file_sizes[fmt] = sample.nbytes * 0.1
        elif fmt == 'png':
            file_sizes[fmt] = sample.nbytes * 0.5
        else:
            file_sizes[fmt] = sample.nbytes

    print("포맷별 예상 파일 크기:")
    for fmt, size in file_sizes.items():
        print(f"{fmt.upper()}: {size/1024:.1f} KB")


demonstrate_format_conversion()
analyze_hsv_channels()
file_format_operations()
