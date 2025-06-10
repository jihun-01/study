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


def demonstrate_filters():
    original = create_sample_image()
    noisy = original.copy()

    noise = np.random.normal(0, 25, original.shape).astype(np.uint8)
    noisy = cv2.add(original, noise)

    filters = {
        '원본': original,
        '노이즈': noisy,
        '가우시안 블러': cv2.GaussianBlur(noisy, (15,15), 0),
        '미디언 필터': cv2.medianBlur(noisy, 5),
        '바이래터럴 필터': cv2.bilateralFilter(noisy, 9, 75, 75),
        '샤프닝' : None
    }

    sharpening_kernel = np.array([
        [-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1]
    ])
    filters['샤프닝'] = cv2.filter2D(original, -1, sharpening_kernel)

    plt.figure(figsize=(18,12))
    plt.rc('font', family='Malgun Gothic')

    for i, (name, filtered_img) in enumerate(filters.items()):
        plt.subplot(2, 3, i+1)
        plt.imshow(cv2.cvtColor(filtered_img, cv2.COLOR_BGR2RGB))
        plt.title(name)
        plt.axis('off')

    plt.tight_layout()
    plt.show()

def edge_detection_filters():
    original = create_sample_image()
    gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

    edges = {
        '원본': gray,
        'sobel X': cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3),
        'sobel Y': cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3),
        'Laplacian': cv2.Laplacian(gray, cv2.CV_64F),
        'Canny': cv2.Canny(gray, 50, 150)
    }

    plt.figure(figsize=(15,6))
    plt.rc('font', family='Malgun Gothic')

    for i, (name, edge_img) in enumerate(edges.items()):
        plt.subplot(1, 5, i+1)

        if name == 'Canny':
            plt.imshow(edge_img, cmap='gray')
        
        elif name == '원본':
            plt.imshow(edge_img, cmap='gray')
        else:
            plt.imshow(np.abs(edge_img), cmap='gray')

        plt.title(name)
        plt.axis('off')

    plt.tight_layout()
    plt.show()

def custom_kernels():

    original = create_sample_image()

    kernels = {
        '원본': None,
        '엠보스': np.array([[-2, -1, 0],
                            [-1, 1, 1],
                            [0, 1, 2]]),
        '아웃라인' : np.array([[-1, -1, -1],
                               [-1, 8, -1],
                               [-1, -1, -1]]),
        '블러' : np.ones((5,5), np.float32) / 25
    }
    
    plt.figure(figsize=(16,4))

    for i,(name,kernel) in enumerate(kernels.items()):
        plt.subplot(1, 4, i+1)

        if kernel is None:
            result = original
        else:
            result = cv2.filter2D(original, -1, kernel)

        plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
        plt.title(name)
        plt.axis('off')
    
    plt.tight_layout()
    plt.show()

demonstrate_filters()
edge_detection_filters()
custom_kernels()
    
