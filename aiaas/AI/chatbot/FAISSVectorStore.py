# pip install faiss-cpu
# pip install faiss-gpu
# FAISS(Facebook AI Similarity Search): Meta에서 개발한 고성능 벡터 유사도 검색 라이브러리
# - faiss-cpu: CPU 버전, 일반적으로 사용
# - faiss-gpu: GPU 버전, 대용량 데이터 처리시 CPU 대비 10-100배 빠른 성능

import faiss  # 벡터 유사도 검색을 위한 고성능 라이브러리
import numpy as np  # 수치 연산을 위한 라이브러리, 벡터 계산에 필수
import os  # 운영체제 환경변수 접근을 위한 모듈
from dotenv import load_dotenv  # .env 파일에서 환경변수 로드
from Openaiembedding import OpenAIEmbedder  # OpenAI API를 사용한 텍스트 임베딩 클래스

load_dotenv()  # .env 파일에서 환경변수를 로드 (OPENAI_API_KEY 등)

class FAISSVectorStore:
    """
    FAISS를 사용한 벡터 저장소 클래스
    - 텍스트를 임베딩 벡터로 변환하여 저장
    - 유사도 기반 빠른 검색 기능 제공
    - 메모리 효율적인 벡터 인덱싱
    """
    
    def __init__(self, dimension):
        """
        FAISS 벡터 저장소 초기화
        """
        self.dimension = dimension
        # dimension: 모든 벡터가 같은 차원을 가져야 FAISS 인덱스에 저장 가능
        
        self.index = faiss.IndexFlatIP(dimension)  # Inner Product 인덱스 생성
        # 벡터 A와 B의 내적: A·B = |A| * |B| * cos(theta)
        # 따라서 A와 B를 정규화(|A| = |B| = 1)하면, A·B = cos(theta) → 코사인 유사도와 동일해짐
        # 즉, 벡터 정규화를 통해 내적을 코사인 유사도로 변환 가능
        # 특징:
        # "Flat"은 모든 벡터를 정확히 비교하는 방식 (근사 검색이 아님)
        # IndexFlatL2: L2 거리 기반 유사도 계산
        # IndexIVFFlat: 근사 검색을 위한 인덱스 (대규모 검색 시 유리)
        # IndexFlatIP를 코사인 유사도 계산에 사용하려면 입력 벡터들을 반드시 L2 정규화해야 함
        #   (ex. faiss.normalize_L2(vectors))
        # 생성한 인덱스는 추후 검색 시 유사도 계산에 활용됨

        self.documents = []  # 원본 문서 텍스트 저장 리스트
        # documents: 검색 결과 반환시 원본 텍스트를 보여주기 위해 저장
        
        self.document_ids = []  # 문서 고유 ID 저장 리스트
        # document_ids: 각 문서를 식별하기 위한 고유 ID (사용자 정의 가능)
    
    def add_documents(self, documents, embeddings, document_ids=None):
        """
        문서와 임베딩을 인덱스에 추가하는 메소드
        """
        # 임베딩 정규화 (코사인 유사도 계산을 위해)
        embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)
        # np.linalg.norm: 벡터의 크기(magnitude) 계산
        # axis=1: 각 행(문서)별로 정규화
        # keepdims=True: 차원 유지 (나눗셈 연산을 위해)
        # 정규화 이유: 내적이 코사인 유사도가 되도록 벡터 크기를 1로 만듦
        
        # FAISS 인덱스에 임베딩 벡터 추가
        self.index.add(embeddings.astype('float32'))
        # astype('float32'): FAISS는 float32 형식 요구 (메모리 효율성)
        # add(): 벡터들을 인덱스에 추가, 내부적으로 인덱스 번호 자동 할당
        
        # 원본 문서 텍스트 저장
        self.documents.extend(documents)
        # extend(): 리스트의 모든 요소를 기존 리스트에 추가
        # append()와 다름: append는 리스트 자체를 하나의 요소로 추가
        
        # 문서 ID 생성 및 저장
        if document_ids is None:
            # 자동 ID 생성: "doc_시작번호", "doc_시작번호+1", ...
            document_ids = [f"doc_{len(self.documents) - len(documents) + i}" 
                          for i in range(len(documents))]
            # len(self.documents) - len(documents): 이전까지 저장된 문서 수
            # 새로 추가되는 문서들에 대해 연속된 번호 할당
        
        self.document_ids.extend(document_ids)
        # 생성되거나 전달받은 문서 ID들을 저장
        
        print(f"{len(documents)}개 문서가 FAISS 인덱스에 추가되었습니다.")
        # 사용자에게 처리 완료 알림
    
    def search(self, query_embedding, top_k=5):
        """
        주어진 쿼리 임베딩과 유사한 문서들을 검색하는 메소드
        """
        # 쿼리 임베딩 정규화 (저장된 문서 임베딩과 동일한 방식)
        query_embedding = query_embedding / np.linalg.norm(query_embedding)
        # 정규화 이유: 코사인 유사도 계산을 위해 벡터 크기를 1로 만듦
        
        # FAISS 검색을 위한 형태 변환
        query_embedding = query_embedding.reshape(1, -1).astype('float32')    
        # FAISS는 (배치 크기, 벡터 차원)의 2D 배열을 입력으로 요구함
        # 질문이 1개이므로 배치 크기 1로 변환
        # reshape(1, -1): 1D 배열을 2D 배열로 변환 [차원] → [1, 차원]
        # -1: 나머지 차원은 자동 계산
        # astype('float32'): FAISS 요구사항에 맞는 데이터 타입
        
        # FAISS 인덱스에서 유사한 벡터 검색
        scores, indices = self.index.search(query_embedding, top_k)
        # search(): 주어진 쿼리와 가장 유사한 top_k개 벡터 검색
        # top_k: 검색 결과 상위 몇 개 반환
        # 반환값:
        # - scores: 유사도 점수 배열 (정규화된 경우, 코사인 유사도와 동일)
        # - indices: 유사한 벡터들의 인덱스 (self.documents 내 위치)
        
        # 검색 결과를 사용자 친화적 형태로 변환
        results = []
        for score, idx in zip(scores[0], indices[0]):
            # scores[0], indices[0]: 배치 크기가 1(질문 1개)이므로 첫 번째 결과만 사용
            # zip(): 점수와 인덱스를 쌍으로 묶어서 순회
            
            if idx < len(self.documents):
                # 유효한 인덱스인지 확인 
                # FAISS가 잘못된 인덱스를 반환할 가능성은 낮지만 안전성을 위해 체크
                
                results.append({
                    'document': self.documents[idx],      # 원본 문서 텍스트
                    'score': float(score),                # 유사도 점수 (numpy → python float)
                    'document_id': self.document_ids[idx], # 문서 ID
                    'index': int(idx)                     # 인덱스 번호 (numpy → python int)
                })
                # 각 검색 결과를 딕셔너리로 구조화하여 사용자가 쉽게 활용 가능
        
        return results
        # 유사도 순으로 정렬된 검색 결과 반환
        # 질문에 대한 배치 당 top_k개의 결과 반환

# 사용 예제 및 테스트 코드
if __name__ == "__main__":
    # 메인 모듈로 실행될 때만 실행되는 코드
    # import시에는 실행되지 않음 (라이브러리로 사용할 때 방해하지 않음)
    
    # 샘플 문서 데이터 정의
    sample_docs = [
        "딥러닝은 인공신경망을 여러 층으로 쌓아 복잡한 패턴을 학습하는 머신러닝 기법입니다.",
        "머신러닝은 데이터로부터 패턴을 학습하여 예측이나 분류를 수행하는 인공지능 기술입니다.",
        "자연어처리는 컴퓨터가 인간의 언어를 이해하고 처리할 수 있게 하는 기술 분야입니다.",
        "컴퓨터 비전은 컴퓨터가 이미지나 비디오를 해석하고 이해할 수 있게 하는 기술입니다.",
        "강화학습은 에이전트가 환경과 상호작용하며 보상을 최대화하는 방향으로 학습하는 방법입니다."
    ]
    # 5개의 AI/ML 관련 한국어 문서
    # 각각 다른 주제를 다루어 검색 테스트에 적합
    
    # OpenAI API 키 확인
    api_key = os.getenv("OPENAI_API_KEY")
    # OpenAI 임베더 초기화
    embedder = OpenAIEmbedder(api_key)
    # OpenAIEmbedder 클래스 인스턴스 생성
    # API 키를 전달하여 OpenAI API 호출 준비
    
    # 문서들의 임베딩 생성
    print("문서 임베딩 생성 중...")
    doc_embeddings_list = embedder.get_batch_embeddings(sample_docs)
    # get_batch_embeddings(): 여러 문서를 한 번에 임베딩으로 변환
    # API 호출 횟수를 줄여 효율성과 비용 절감
    # 반환값: 임베딩 벡터들의 리스트
    
    if doc_embeddings_list:
        # 임베딩 생성이 성공한 경우
        
        # 리스트를 numpy 배열로 변환
        doc_embeddings = np.array(doc_embeddings_list)
        # numpy 배열로 변환하는 이유:
        # 1. FAISS가 numpy 배열을 요구
        # 2. 수치 연산 (정규화 등)을 위해 필요
        # 3. 메모리 효율성과 연산 속도 향상
        
        # FAISS 벡터 저장소 초기화
        faiss_store = FAISSVectorStore(dimension=doc_embeddings.shape[1])
        # shape[1]: 임베딩 차원 수 (예: 1536)
        # shape[0]: 문서 개수, shape[1]: 각 임베딩의 차원
        
        # 문서들과 임베딩을 저장소에 추가
        faiss_store.add_documents(sample_docs, doc_embeddings)
        # 원본 문서와 해당 임베딩을 함께 저장
        # 이후 검색시 원본 텍스트도 함께 반환 가능
        
        # 검색 쿼리 처리
        print("\n검색 실행 중...")
        query_embedding_list = embedder.get_embedding("딥러닝 학습 방법")
        # 단일 질문에 대한 임베딩 생성
        # "딥러닝 학습 방법"과 유사한 문서들을 찾기 위한 쿼리
        
        if query_embedding_list:
            # 쿼리 임베딩 생성이 성공한 경우
            
            query_embedding = np.array(query_embedding_list)
            # 리스트를 numpy 배열로 변환 (FAISS 검색을 위해)
            
            # 유사도 검색 실행
            fast_results = faiss_store.search(query_embedding, top_k=3)
            # top_k=3: 가장 유사한 상위 3개 문서 반환
            # 작은 데이터셋이므로 3개로 제한
            
            # 검색 결과 출력
            print("\nFAISS 빠른 검색 결과:")
            for i, result in enumerate(fast_results, 1):
                # enumerate(start=1): 1부터 시작하는 순서 번호
                print(f"{i}. 점수: {result['score']:.3f}")
                # :.3f: 소수점 3자리까지 표시
                print(f"   문서: {result['document']}")
                # 원본 문서 텍스트 출력
                print(f"   ID: {result['document_id']}")
                # 문서 고유 ID 출력
                print()
                # 가독성을 위한 빈 줄
        else:
            # 쿼리 임베딩 생성 실패
            print("질문 임베딩 생성에 실패했습니다.")
            # OpenAI API 호출 오류, 네트워크 문제, API 키 문제 등
    else:
        # 문서 임베딩 생성 실패
        print("문서 임베딩 생성에 실패했습니다.")
        # 원인: API 오류, 네트워크 문제, 할당량 초과 등