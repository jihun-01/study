import cv2
import matplotlib.pyplot as plt

sample_image = cv2.imread('image.png')

blue_channel = sample_image[:, :, 0]
green_channel = sample_image[:, :, 1]
red_channel = sample_image[:, :, 2]

plt.figure(figsize=(15, 3))
plt.rc('font', family='Malgun Gothic')
plt.subplot(1, 4, 1)
plt.imshow(cv2.cvtColor(sample_image, cv2.COLOR_BGR2RGB))
plt.title('원본 이미지')
plt.axis('off')

plt.subplot(1, 4, 2)
plt.imshow(red_channel, cmap='Reds')
plt.title('Red 채널')
plt.axis('off')

plt.subplot(1, 4, 3)
plt.imshow(green_channel, cmap='Greens')
plt.title('Green 채널')
plt.axis('off')

plt.subplot(1, 4, 4)
plt.imshow(blue_channel, cmap='Blues')
plt.title('Blue 채널')
plt.axis('off')

plt.tight_layout()
plt.show()



