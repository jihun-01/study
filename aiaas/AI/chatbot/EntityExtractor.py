import spacy

class EntityExtractor:

    def __init__(self, lang='ko_core_news_sm'):

        try:
            self.nlp = spacy.load(lang)
            #언어 모듈 로드
        
        except OSError:
            self.nlp = spacy.load('en_core_web_sm')
            #한국어 모델 로드 실패시 영어모듈 사용
    
    def extract_entities(self, text):
        doc = self.nlp(text)

        entities = []

        for ent in doc.ents:
            entities.append({
                'text': ent.text,
                'label': ent.label_,
                'start': ent.start_char,
                'end': ent.end_char,
                'description': spacy.explain(ent.label_)
            })

        return entities
    
if __name__ == '__main__':
    extractor = EntityExtractor()
    text = "김철수는 내일 오후 3시에 서울역에서 만나자고 했다"

    entities = extractor.extract_entities(text)

    for entity in entities:
        print(f"개체: {entity['text']}, 유형: {entity['label']}, 설명: {entity['description']}")
