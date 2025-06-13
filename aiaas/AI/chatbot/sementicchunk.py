import re

def simple_sentence_split(text):
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences

def semantic_chunking(text, max_sentences=3):
    sentences = simple_sentence_split(text)
    chunks = []
    current_chunk = []
    for sentence in sentences:
        current_chunk.append(sentence)
        if len(current_chunk) >= max_sentences:
            chunks.append('. '.join(current_chunk) + '.')
            current_chunk = []
    if current_chunk:
        chunks.append('. '.join(current_chunk) + '.')
    return chunks

sample_text = """
머신러닝은 데이터를 기반으로 하는 컴퓨터 시스템의 학습 능력을 개선하는 혁신적인 기술로, 명시적인 프로그래밍 없이도 데이터의 패턴을 찾아내어 예측과 분류 작업을 수행할 수 있습니다.

전통적인 프로그래밍에서는 개발자가 모든 규칙과 조건을 직접 코딩해야 했지만, 머신러닝은 대량의 데이터로부터 자동으로 규칙을 학습하여 새로운 데이터에 대한 인사이트를 제공합니다.

머신러닝의 주요 분야로는 지도학습, 비지도학습, 강화학습이 있으며, 각각 다른 접근 방식으로 문제를 해결합니다. 지도학습은 레이블이 있는 데이터를 사용하여 분류나 회귀 작업을 수행하고, 비지도학습은 레이블이 없는 데이터에서 숨겨진 패턴을 발견하며, 강화학습은 환경과의 상호작용을 통해 최적의 행동 전략을 학습합니다.

딥러닝은 머신러닝의 한 분야로, 인공 신경망을 여러 층으로 쌓아 복잡한 패턴을 학습하는 기술입니다. 이미지 인식, 자연어 처리, 음성 인식 등의 분야에서 획기적인 성과를 보여주며, 현재 AI 기술 발전의 핵심 동력이 되고 있습니다. 특히 트랜스포머 아키텍처의 등장으로 대화형 AI와 생성형 AI 기술이 급속도로 발전하고 있습니다.
"""

semantic_chunks = semantic_chunking(sample_text, max_sentences=2)
for i, chunk in enumerate(semantic_chunks):
    print(f"의미 청크 {i+1}: {chunk}")