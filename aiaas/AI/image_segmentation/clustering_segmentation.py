import cv2
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans



image = cv2.imread('image.png')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
pixel_values = image_rgb.reshape(-1, 3)

pixel_values = np.float32(pixel_values)

k = 5
kmeans = KMeans(n_clusters=k, random_state=42)
labels = kmeans.fit_predict(pixel_values)

centers = np.uint8(kmeans.cluster_centers_)

segmented_image = centers[labels.flatten()]

segmented_image = segmented_image.reshape(image_rgb.shape)

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.imshow(image_rgb)
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 3, 2)
plt.imshow(segmented_image)
plt.title('Segmented Image')
plt.axis('off')

plt.tight_layout()
plt.show()





