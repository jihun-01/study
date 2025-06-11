import cv2
import matplotlib.pyplot as plt


image = cv2.imread('testimage.png', 0)

ret, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)


ret2, otsu = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

adaptive = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

plt.figure(figsize=(15, 5))
plt.subplot(1, 4, 1)
plt.imshow(image, cmap='gray')
plt.title('Original')
plt.axis('off')

plt.subplot(1, 4, 2)
plt.imshow(binary, cmap='gray')
plt.title('Binary')
plt.axis('off')

plt.subplot(1, 4, 3)
plt.imshow(otsu, cmap='gray')
plt.title('Otsu')
plt.axis('off')

plt.subplot(1, 4, 4)
plt.imshow(adaptive, cmap='gray')
plt.title('Adaptive')
plt.axis('off')

plt.tight_layout()
plt.show()



