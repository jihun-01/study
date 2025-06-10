import torch
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image, ImageDraw, ImageFont
import numpy as np


class TrOCRSystem:

    def __init__(self, model_name='microsoft/trocr-base-printed'):
        #프로세스 선언
        self.processor = TrOCRProcessor.from_pretrained(model_name)
        # 모델선언
        self.model = VisionEncoderDecoderModel.from_pretrained(model_name)

        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model.to(self.device)

    def extract_text(self, image, return_confidence=False):

        if isinstance(image, np.ndarray):
            image = Image.fromarray(image)
        elif isinstance(image, str):
            image = Image.open(image)

        pixel_values = self.processor(image, return_tensors='pt').pixel_values
        pixel_values = pixel_values.to(self.device)

        with torch.no_grad():
            outputs = self.model.generate(
                pixel_values,
                return_dict=True,
                output_scores=True,
                max_langth=256
            )
            Generated_ids = outputs.sequences
            token_scores = outputs.scores
        
        generated_text = self.processor.batch_decode(Generated_ids, skip_special_tokens=True)
        
        if return_confidence:
            if token_scores:
                token_probs = []
                for score in token_scores:
                    probs = torch.softmax(score, dim=-1)
                    max_prob = torch.max(probs).item()
                    token_probs.append(max_prob)
                confidence = sum(token_probs) / len(token_probs) if token_probs else 0.0

                print(f"confidence: {confidence}")
            else:
                confidence = 0.5
                print("실제 확률 정보 없음")
            return generated_text, confidence
        
        return generated_text
    
    
        
        
        
        
        
        
    
        
        


# 샘플 이미지 생성
def create_sample_trocr_image():
    img = Image.new('RGB', (400,100),'white')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('arial.ttf', 24)
    text = 'TrOCR Demo Text'
    draw.text((50, 30), text, fill = 'black', font = font)
    img.save('sample_trocr_image.png')
    return img






ocr = TrOCRSystem()

sample_image = create_sample_trocr_image()

text = ocr.extract_text(sample_image)
print(f'인식된 텍스트: {text}')





