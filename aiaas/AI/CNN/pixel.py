import numpy as np
import matplotlib.pyplot as plt

simple_image = np.array([
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
    [[255, 255, 0], [255, 0, 255], [0, 255, 255]],
    [[0, 0, 0], [128, 128, 128], [255, 255, 255]]
], dtype=np.uint8)


plt.rc('font', family='Malgun Gothic')
plt.figure(figsize=(8, 4))
plt.imshow(simple_image)
plt.title('3*3 픽셀 이미지')
plt.axis('off')
plt.show()







