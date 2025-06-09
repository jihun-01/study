import cv2
import pytesseract
import numpy as np
import matplotlib.pyplot as plt

def create_sample_image():
    image = np.ones((200, 600, 3), dtype=np.uint8) * 255

    font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    cv2.putText(image, 'Hello OCR World', (50,100), font,2, (0,0,0),3)
    cv2.putText(image, 'This is test image', (50,150), font,1, (0,0,0),2)

    cv2.imwrite('sample_text.png', image)
    return image

def basic_ocr_exaple():
    image_path = 'sample_text.png'
    image = cv2.imread(image_path)
    if image is None:
        image = create_sample_image()

    text = pytesseract.image_to_string(image, lang='eng')

    return text, image

print('기본 예제')
text, image = basic_ocr_exaple()
print(f'text: {text}')
