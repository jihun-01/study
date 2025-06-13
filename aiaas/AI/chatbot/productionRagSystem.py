import os
from datetime import datetime
from typing import List, Dict, Optional
import time
from dotenv import load_dotenv
import numpy as np

# 기존 구현된 클래스들 import
from FAISSVectorStore import FAISSVectorStore
from Openaiembedding import OpenAIEmbedder
from OpenAIChatbot import OpenAIChatbot
from EntityExtractor import EntityExtractor

load_dotenv()

class EnhancedProductionRAGSystem:
    """
    개선된 프로덕션 환경용 GPT-RAG 통합 시스템
    기존 구현된 클래스들을 활용한 모듈화된 아키텍처:
    - FAISSVectorStore: 고성능 벡터 검색
    - OpenAIEmbedder: 임베딩 생성
    - OpenAIChatbot: 대화형 인터페이스
    - EntityExtractor: 쿼리 개체 추출
    """
    
    def __init__(self, openai_api_key: str, gpt_model: str = "gpt-4.1-nano", 
                 embedding_model: str = "text-embedding-3-small"):
        """
        시스템 초기화
        """
        # 클래스 변수 초기화
        # openai_api_key: OpenAI API 서비스 접근을 위한 인증 키
        # gpt_model: 답변 생성에 사용할 GPT 모델명 (기본값: gpt-3.5-turbo)
        # embedding_model: 텍스트를 벡터로 변환할 임베딩 모델명
        self.api_key = openai_api_key
        self.gpt_model = gpt_model
        self.embedding_model = embedding_model
        
        # 1. 임베딩 엔진 초기화
        self.embedder = OpenAIEmbedder(api_key=openai_api_key)
        # OpenAIEmbedder: 텍스트를 벡터로 변환하는 임베딩 생성 전담 클래스
        # 단일 책임 원칙에 따라 임베딩 생성만 담당
        self.embedder.model = embedding_model  # 모델 설정 변경
        # 사용할 임베딩 모델을 동적으로 설정 (기본값에서 사용자 지정값으로 변경)
        
        # 2. 벡터 저장소 초기화 (나중에 문서 추가 시 설정)
        self.vector_store = None
        # FAISSVectorStore 인스턴스를 저장할 변수
        # None으로 초기화하는 이유: 임베딩 차원을 알아야 FAISS 인덱스 생성 가능
        self.dimension = 1536  # text-embedding-3-small 차원
        # OpenAI text-embedding-3-small 모델의 기본 출력 차원
        # 실제로는 첫 번째 문서 임베딩 시 동적으로 확인하여 설정
        
        # 3. 챗봇 엔진 초기화
        self.chatbot = OpenAIChatbot(api_key=openai_api_key, model=gpt_model)
        # OpenAIChatbot: 대화 관리 및 OpenAI API 호출을 담당하는 클래스
        # 대화 기록 유지, 시스템 프롬프트 관리, API 호출 등을 전담
        
        # 4. 개체 추출기 초기화
        try:
            self.entity_extractor = EntityExtractor()
            # EntityExtractor: spaCy 기반 개체명 인식(NER) 기능 제공
            # 질문에서 사람명, 지명, 조직명, 날짜 등을 자동 추출
        except Exception as e:
            print(f"EntityExtractor 초기화 실패: {e}")
            self.entity_extractor = None
            # 개체 추출기 초기화 실패 시에도 시스템이 계속 작동하도록 None으로 설정
            # spaCy 모델이 설치되지 않은 환경에서도 RAG 시스템의 핵심 기능은 유지
        
        # 문서 메타데이터 저장
        self.documents_metadata = []
        # 각 문서의 메타데이터(출처, 제목, 저자 등)를 저장하는 리스트
        # 검색 결과와 원본 문서 정보를 매핑하기 위해 필요
        
        # RAG 전용 시스템 프롬프트 설정
        self._setup_rag_prompt()
        # 챗봇에 RAG 시스템에 특화된 시스템 프롬프트를 설정하는 private 메소드 호출
        
        print("Enhanced RAG System 초기화 완료!")
        print(f"   GPT 모델: {self.gpt_model}")
        print(f"   임베딩 모델: {self.embedding_model}")
        print(f"   벡터 DB: FAISS")
        print(f"   개체 추출: {'활성화' if self.entity_extractor else '비활성화'}")
        # 시스템 초기화 완료 상태를 사용자에게 알리는 출력
        # 각 컴포넌트의 설정 상태를 명시적으로 표시
    
    def _setup_rag_prompt(self):
        """RAG 시스템용 프롬프트 설정"""
        # private 메소드 (_로 시작): 클래스 내부에서만 사용되는 메소드
        # RAG 시스템에 특화된 시스템 프롬프트를 구성하여 챗봇에 설정
        rag_prompt = """당신은 주어진 문서를 바탕으로 정확하고 도움이 되는 답변을 제공하는 AI 어시스턴트입니다.

핵심 지침:
1. 주어진 참고 문서의 내용만을 바탕으로 답변하세요
2. 문서에 없는 내용은 추측하거나 만들어내지 마세요
3. 답변의 근거가 되는 문서 부분을 명시하세요
4. 확실하지 않은 내용은 "제공된 문서에서 찾을 수 없습니다"라고 말하세요
5. 답변은 친근하고 이해하기 쉽게 작성하세요
6. 질문과 직접 관련된 내용만 답변하세요

답변 형식:
- 주요 답변을 먼저 제시하세요
- 관련된 추가 정보가 있다면 부연 설명하세요
- 참고한 문서를 명시하세요 (예: "[참고문서 1]에 따르면...")
"""
        # RAG 시스템의 핵심 동작 원칙을 정의한 프롬프트
        # 환각(hallucination) 방지를 위해 문서 기반 답변만 하도록 제한
        # 답변의 신뢰성 확보를 위해 출처 명시를 요구
        self.chatbot.set_system_prompt(rag_prompt)
        # OpenAIChatbot 인스턴스의 시스템 프롬프트를 RAG 전용으로 설정
        # 이후 모든 대화에서 이 프롬프트가 기본 지침으로 작동
    
    def add_documents(self, documents: List[str], metadatas: Optional[List[Dict]] = None):
        """
        문서들을 지식 베이스에 추가
        """
        # documents: 실제 문서 내용이 담긴 문자열 리스트
        # 각 요소는 하나의 문서를 나타내며, 임베딩 생성 및 검색의 대상이 됨
        # metadatas: 각 문서에 대한 추가 정보 (출처, 제목, 저자, 날짜 등)
        # Optional[List[Dict]]: 선택적 매개변수로 None일 경우 기본값 생성
        print(f"{len(documents)}개 문서 처리 중...")
        start_time = time.time()
        # 처리 시간 측정을 위한 시작 시간 기록
        # 프로덕션 환경에서 성능 모니터링을 위해 필요
        
        # 1. 임베딩 생성
        print("문서 임베딩 생성 중...")
        doc_embeddings_list = self.embedder.get_batch_embeddings(documents)
        # get_batch_embeddings: 여러 문서를 한 번에 임베딩으로 변환
        # 개별 API 호출보다 효율적이며 비용 절감 효과
        # 반환값: 각 문서에 대응하는 임베딩 벡터들의 리스트
        
        if not doc_embeddings_list:
            print("임베딩 생성에 실패했습니다.")
            return False
        # 임베딩 생성 실패 시 조기 반환
        # API 오류, 네트워크 문제, 할당량 초과 등의 상황 처리
        
        embedding_time = time.time() - start_time
        # 임베딩 생성에 소요된 시간 계산
        # 성능 분석 및 사용자 피드백을 위해 측정
        
        # 2. 메타데이터 기본값 설정
        if metadatas is None:
            metadatas = [
                {
                    "source": f"document_{i}", 
                    "timestamp": datetime.now().isoformat(),
                    # isoformat 예시 : 2025-06-13T10:00:00.000000
                    "index": i
                } 
                for i in range(len(documents))
            ]
        # 메타데이터가 제공되지 않은 경우 기본값 자동 생성
        # source: 문서 식별을 위한 고유 이름
        # timestamp: 문서 추가 시점 기록 (ISO 8601 형식)
        # index: 문서의 순서 번호
        
        # 3. 벡터 저장소 초기화 (첫 번째 문서 추가 시)
        if self.vector_store is None:
            # 임베딩 차원 확인
            if doc_embeddings_list:
                self.dimension = len(doc_embeddings_list[0])
                # dimension = embeddings.shape[1]  # 이렇게 해도 됨
                # 왜 1이 아닌 0번째 인덱스인지 설명 추가:
                # 임베딩 벡터 리스트의 첫 번째 요소(doc_embeddings_list[0])의 길이를 차원으로 설정
                # 이 값은 모든 문서의 임베딩 벡터가 동일한 차원을 가져야 하므로 첫 번째 벡터의 차원을 사용
                # 예를 들어, 모든 문서의 임베딩 벡터가 1536차원이라면, self.dimension은 1536이 됨
            # 실제 생성된 임베딩의 차원 수를 확인하여 정확한 값 설정
            # 모델에 따라 차원이 다를 수 있으므로 동적 확인 필요
            
            self.vector_store = FAISSVectorStore(dimension=self.dimension)
            # FAISS 인덱스는 생성 시 벡터 차원을 알아야 하므로 지연 초기화
            print(f"FAISS 벡터 저장소 생성 (차원: {self.dimension})")
        
        # 4. 문서와 임베딩을 벡터 저장소에 추가

        doc_embeddings = np.array(doc_embeddings_list)
        # 리스트를 numpy 배열로 변환
        # FAISS가 numpy 배열을 요구하며, 수치 연산 최적화를 위해 필요
        
        # 문서 ID 생성
        doc_ids = [f"doc_{len(self.documents_metadata) + i}" for i in range(len(documents))]
        # 각 문서에 고유한 ID 부여
        # 기존 문서 수를 기준으로 연속된 번호 할당하여 중복 방지
        
        # 벡터 저장소에 추가
        self.vector_store.add_documents(documents, doc_embeddings, doc_ids)
        # FAISSVectorStore의 add_documents 메소드 호출
        # 원본 문서, 임베딩 벡터, 문서 ID를 함께 저장
        # 이후 검색 시 인덱스를 통해 원본 문서 정보 제공 가능
        
        # 메타데이터 저장
        self.documents_metadata.extend(metadatas)
        # 메타데이터를 클래스 변수에 저장
        # 검색 결과 반환 시 문서의 상세 정보 제공을 위해 필요
        
        total_time = time.time() - start_time
        # 전체 처리 시간 계산 (임베딩 생성 + FAISS 인덱싱 + 메타데이터 저장)
        print(f"문서 추가 완료!")
        print(f"   임베딩 생성 시간: {embedding_time:.2f}초")
        print(f"   총 처리 시간: {total_time:.2f}초")
        print(f"   저장된 총 문서: {len(self.documents_metadata)}개")
        # 사용자에게 처리 완료 상태와 성능 정보 제공
        
        return True
        # 성공적으로 완료되었음을 반환
        # 호출하는 측에서 성공/실패 여부를 확인 가능
    
    def search_documents(self, query: str, top_k: int = 5) -> List[Dict]:
        """
        질문과 관련된 문서 검색
        """
        # query: 사용자가 입력한 자연어 질문
        # 이 질문을 기반으로 관련성이 높은 문서들을 찾음
        # top_k: 검색 결과로 반환할 최대 문서 개수
        # 기본값 5는 답변 생성에 적절한 문서 수를 고려한 설정
        if self.vector_store is None:
            print("저장된 문서가 없습니다.")
            return []
        # 벡터 저장소가 초기화되지 않은 경우 빈 리스트 반환
        # 문서를 추가하지 않은 상태에서 검색을 시도할 때 발생
        
        # 1. 개체 추출 (선택적)
        entities = []
        if self.entity_extractor:
            try:
                entities = self.entity_extractor.extract_entities(query)
                # extract_entities: 질문에서 개체명(사람, 장소, 조직 등) 추출
                # 반환값: 각 개체의 텍스트, 타입, 위치 정보를 담은 딕셔너리 리스트
                if entities:
                    print(f"추출된 개체: {[ent['text'] for ent in entities]}")
                # 추출된 개체가 있을 경우 사용자에게 정보 제공
                # 디버깅 및 쿼리 분석 결과 확인을 위함
            except Exception as e:
                print(f"개체 추출 오류: {e}")
        # 개체 추출기가 없거나 오류 발생 시에도 검색은 계속 진행
        # 개체 추출은 부가 기능이므로 실패해도 핵심 기능에 영향 없음
        
        # 2. 쿼리 임베딩 생성
        query_embedding_list = self.embedder.get_embedding(query)
        # get_embedding: 단일 텍스트(질문)를 임베딩 벡터로 변환
        # 문서들과 동일한 임베딩 모델을 사용하여 같은 벡터 공간에서 비교 가능
        if not query_embedding_list:
            print("쿼리 임베딩 생성에 실패했습니다.")
            return []
        # 쿼리 임베딩 생성 실패 시 검색 불가능하므로 빈 결과 반환
        
        import numpy as np
        query_embedding = np.array(query_embedding_list)
        # 리스트를 numpy 배열로 변환
        # FAISS 검색을 위해 numpy 배열 형태 필요
        
        # 3. 벡터 검색 수행
        search_results = self.vector_store.search(query_embedding, top_k)
        # FAISS 기반 코사인 유사도 검색 실행
        # 반환값: 유사도 점수와 함께 정렬된 문서들의 정보
        
        # 4. 결과 포맷팅
        formatted_results = []
        for i, result in enumerate(search_results):
            # 메타데이터 인덱스 찾기
            doc_index = None
            for idx, doc_id in enumerate(self.vector_store.document_ids):
                if doc_id == result['document_id']:
                    doc_index = idx
                    break
            # FAISS 검색 결과의 문서 ID를 이용해 메타데이터 배열에서 해당 인덱스 찾기
            # 벡터 저장소와 메타데이터 배열 간의 매핑을 위해 필요
            
            metadata = self.documents_metadata[doc_index] if doc_index is not None else {}
            # 찾은 인덱스를 통해 해당 문서의 메타데이터 가져오기
            # 인덱스를 찾지 못한 경우 빈 딕셔너리 반환
            
            formatted_results.append({
                'content': result['document'],          # 원본 문서 텍스트
                'metadata': metadata,                   # 문서 메타데이터 (출처, 제목 등)
                'similarity_score': result['score'],   # 유사도 점수 (높을수록 관련성 높음)
                'rank': i + 1,                         # 검색 결과 순위 (1부터 시작)
                'document_id': result['document_id'],   # 문서 고유 ID
                'entities_in_query': entities          # 쿼리에서 추출된 개체 정보
            })
            # 검색 결과를 구조화된 형태로 변환
            # 후속 처리(컨텍스트 구성, 답변 생성)에서 활용하기 위한 표준 형식
        
        return formatted_results
        # 검색된 문서들의 상세 정보를 포함한 리스트 반환
        # 각 문서는 내용, 메타데이터, 유사도, 순위 등의 정보 포함
    
    def generate_rag_response(self, query: str, top_k: int = 5, 
                            use_chat_history: bool = True) -> Dict:
        """
        RAG 시스템을 통한 답변 생성        
        """
        # query: 답변을 생성할 사용자의 자연어 질문
        # top_k: 참고할 문서의 최대 개수 (많을수록 풍부한 정보, 적을수록 집중된 답변)
        # use_chat_history: 이전 대화 내용을 고려할지 여부
        # True시 연속 대화, False시 독립적 질문으로 처리
        start_time = time.time()
        # 전체 RAG 파이프라인 처리 시간 측정 시작
        print(f"질문 분석: {query}")
        
        # 1. 관련 문서 검색
        retrieved_docs = self.search_documents(query, top_k)
        # search_documents 메소드를 통해 질문과 관련성이 높은 문서들 검색
        # 반환된 문서들이 답변 생성의 근거 자료가 됨
        
        if not retrieved_docs:
            return {
                'query': query,
                'answer': "죄송합니다. 관련된 문서를 찾을 수 없습니다.",
                'retrieved_documents': [],
                'entities': [],
                'processing_time': time.time() - start_time,
                'timestamp': datetime.now().isoformat()
            }
        # 검색 결과가 없는 경우 기본 응답 구조 반환
        # 시스템의 일관성을 위해 동일한 응답 형식 유지
        
        print(f"{len(retrieved_docs)}개 관련 문서 발견")
        
        # 2. 컨텍스트 구성
        context = self._build_context(retrieved_docs)
        # 검색된 문서들을 GPT가 이해할 수 있는 구조화된 형태로 변환
        # 각 문서의 출처와 유사도 정보도 함께 포함
        
        # 3. RAG 프롬프트 생성
        rag_prompt = self._build_rag_prompt(query, context)
        # 질문과 검색된 문서들을 결합하여 GPT에게 전달할 최종 프롬프트 생성
        # 문서 기반 답변을 유도하는 구조화된 프롬프트
        
        # 4. 대화 기록 초기화 (필요 시)
        if not use_chat_history:
            self.chatbot.clear_history()
        # use_chat_history가 False인 경우 이전 대화 기록 삭제
        # 독립적인 질문으로 처리하고 싶을 때 사용
        
        # 5. 챗봇을 통한 답변 생성
        print("RAG 답변 생성 중...")
        try:
            answer = self.chatbot.get_response(rag_prompt)
            # OpenAIChatbot의 get_response 메소드를 통해 GPT API 호출
            # 구조화된 프롬프트를 전달하여 문서 기반 답변 생성
        except Exception as e:
            print(f"답변 생성 오류: {e}")
            answer = f"죄송합니다. 답변 생성 중 오류가 발생했습니다: {e}"
        # API 호출 실패, 네트워크 오류 등 예외 상황 처리
        # 사용자에게 친화적인 오류 메시지 제공
        
        # 6. 개체 정보 수집
        entities = retrieved_docs[0].get('entities_in_query', []) if retrieved_docs else []
        # 첫 번째 검색 결과에서 추출된 개체 정보 가져오기
        # 모든 검색 결과는 동일한 쿼리에서 추출된 개체 정보를 가지므로 첫 번째 것만 사용
        
        # 7. 결과 구성
        result = {
            'query': query,                                    # 원본 질문
            'answer': answer,                                  # 생성된 답변
            'retrieved_documents': retrieved_docs,             # 참고한 문서들
            'entities': entities,                              # 추출된 개체 정보
            'sources_used': len(retrieved_docs),              # 사용된 문서 수
            'processing_time': time.time() - start_time,      # 총 처리 시간
            'timestamp': datetime.now().isoformat(),          # 답변 생성 시각
            'model_info': {                                    # 모델 정보
                'gpt_model': self.gpt_model,
                'embedding_model': self.embedding_model,
                'vector_store': 'FAISS'
            }
        }
        # RAG 시스템의 모든 처리 결과를 구조화된 딕셔너리로 구성
        # 답변뿐만 아니라 처리 과정의 모든 정보를 포함하여 투명성 제공
        
        print(f"RAG 답변 생성 완료 ({result['processing_time']:.2f}초)")
        return result
    
    def _build_context(self, retrieved_docs: List[Dict]) -> str:
        """검색된 문서들로 컨텍스트 구성"""
        # private 메소드: 내부에서만 사용되는 컨텍스트 구성 함수
        # retrieved_docs: search_documents에서 반환된 검색 결과
        context = "=== 참고 문서 ===\n\n"
        # 문서 섹션의 시작을 명확히 표시하는 헤더
        
        for i, doc in enumerate(retrieved_docs, 1):
            source = doc['metadata'].get('source', f'문서 {i}')
            # 메타데이터에서 문서 출처 정보 추출, 없으면 기본값 사용
            similarity = doc['similarity_score']
            # 검색 시 계산된 유사도 점수 (0~1 범위, 높을수록 관련성 높음)
            content = doc['content']
            # 실제 문서 내용 텍스트
            
            context += f"[참고문서 {i}] {source} (유사도: {similarity:.3f})\n"
            context += f"{content}\n\n"
            # 각 문서를 번호, 출처, 유사도와 함께 구조화하여 배치
            # GPT가 각 문서를 구분하고 참조하기 쉽도록 명확한 형식 사용
        
        return context
        # GPT에게 전달할 완성된 컨텍스트 문자열 반환
    
    def _build_rag_prompt(self, query: str, context: str) -> str:
        """RAG용 프롬프트 구성"""
        # query: 사용자의 원본 질문
        # context: _build_context에서 생성된 구조화된 문서 정보
        prompt = f"""
{context}

=== 질문 ===
{query}

위의 참고 문서를 바탕으로 질문에 대한 정확하고 도움이 되는 답변을 작성해주세요.
"""
        # 문서 → 질문 → 답변 요청 순서로 구성
        # GPT가 문서를 먼저 읽고 질문을 이해한 후 답변하도록 유도
        # 문서 기반 답변을 명시적으로 요청
        return prompt
    
    def chat_interface(self):
        """향상된 대화형 인터페이스"""
        # 사용자와 시스템 간의 실시간 대화를 제공하는 메인 인터페이스
        # 명령줄 기반의 대화형 루프 구현
        print("\n" + "="*60)
        print("Enhanced RAG 챗봇이 준비되었습니다!")
        print("   지식 베이스:", f"{len(self.documents_metadata)}개 문서" if self.documents_metadata else "비어있음")
        print("   개체 추출:", "활성화" if self.entity_extractor else "비활성화")
        print("   대화 기록:", "유지됨")
        print("   종료: 'quit', 'exit', '종료' 입력")
        print("   기록 초기화: 'clear' 입력")
        print("="*60)
        # 사용자에게 시스템 상태와 사용 방법을 안내
        # 현재 설정된 지식 베이스 크기, 기능 활성화 상태 등을 표시
        
        while True:
            # 무한 루프를 통한 연속적인 대화 처리
            try:
                user_input = input("\n질문: ").strip()
                # 사용자 입력 받기 및 앞뒤 공백 제거
                
                if user_input.lower() in ['quit', 'exit', '종료']:
                    print("RAG 챗봇을 종료합니다.")
                    break
                # 종료 명령어 확인 (대소문자 구분 없음)
                
                if user_input.lower() == 'clear':
                    self.chatbot.clear_history()
                    print("대화 기록이 초기화되었습니다.")
                    continue
                # 대화 기록 초기화 명령어 처리
                # 새로운 대화를 시작하고 싶을 때 사용
                
                if not user_input:
                    continue
                # 빈 입력인 경우 다시 입력 대기
                
                # RAG 응답 생성
                result = self.generate_rag_response(user_input, use_chat_history=True)
                # use_chat_history=True로 설정하여 이전 대화 맥락 유지
                
                # 답변 출력
                print(f"\n답변: {result['answer']}")
                
                # 처리 정보 출력
                print(f"\n처리 정보:")
                print(f"   참고 문서: {result['sources_used']}개")
                print(f"   처리 시간: {result['processing_time']:.2f}초")
                # 사용자에게 답변과 함께 처리 통계 정보 제공
                
                # 개체 정보 출력 (있는 경우)
                if result['entities']:
                    print(f"   추출된 개체: {', '.join([ent['text'] for ent in result['entities']])}")
                # 질문에서 추출된 개체가 있을 경우 추가 정보로 표시
                
            except KeyboardInterrupt:
                print("\nRAG 챗봇을 종료합니다.")
                break
            # Ctrl+C 입력 시 정상 종료
            except Exception as e:
                print(f"오류 발생: {e}")
            # 기타 예외 발생 시에도 시스템이 중단되지 않고 계속 실행
    
    def get_system_stats(self) -> Dict:
        """시스템 통계 정보 반환"""
        # 현재 시스템의 상태와 설정 정보를 구조화된 형태로 반환
        # 모니터링, 디버깅, 시스템 관리를 위한 정보 제공
        return {
            'total_documents': len(self.documents_metadata),        # 총 저장된 문서 수
            'vector_dimension': self.dimension,                     # 벡터 차원 수
            'models': {                                             # 사용 중인 모델 정보
                'gpt_model': self.gpt_model,
                'embedding_model': self.embedding_model
            },
            'components': {                                         # 각 컴포넌트 상태
                'vector_store': 'FAISS',
                'embedder': 'OpenAI',
                'chatbot': 'OpenAI',
                'entity_extractor': 'spaCy' if self.entity_extractor else None
            },
            'chat_history_length': len(self.chatbot.conversation_history)  # 현재 대화 기록 길이
        }
        # 시스템의 모든 주요 상태 정보를 포함한 딕셔너리 반환
        # 운영 환경에서 시스템 모니터링 및 성능 분석에 활용

# 데모 실행
if __name__ == "__main__":
    # 메인 모듈로 실행될 때만 실행되는 데모 코드
    # 라이브러리로 import될 때는 실행되지 않음
    
    # API 키 확인
    api_key = os.environ.get("OPENAI_API_KEY")
    # 환경변수에서 OpenAI API 키 로드
    # 보안을 위해 코드에 직접 하드코딩하지 않고 환경변수 사용
    if not api_key:
        print("OPENAI_API_KEY 환경변수를 설정해주세요.")
        exit(1)
    # API 키가 없는 경우 프로그램 종료
    # OpenAI API 호출이 불가능하므로 실행 의미 없음
    
    # 향상된 RAG 시스템 초기화
    rag_system = EnhancedProductionRAGSystem(api_key)
    # 시스템 인스턴스 생성 및 모든 컴포넌트 초기화
    
    # 지식 베이스 구축
    documents = [
        "인공지능(AI)은 인간의 지능을 모방하는 컴퓨터 시스템입니다. 학습, 추론, 문제 해결 등의 능력을 갖추고 있습니다. 현대 AI는 딥러닝과 머신러닝 기술을 기반으로 발전하고 있습니다.",
        "머신러닝은 AI의 핵심 분야로, 데이터로부터 패턴을 학습하여 예측이나 결정을 내리는 방법입니다. 지도학습, 비지도학습, 강화학습으로 분류됩니다.",
        "딥러닝은 머신러닝의 세부 분야로, 인공 신경망을 여러 층으로 쌓아 복잡한 패턴을 학습합니다. 이미지 인식, 자연어 처리 등에서 뛰어난 성능을 보입니다.",
        "자연어 처리(NLP)는 컴퓨터가 인간의 언어를 이해하고 처리할 수 있게 하는 AI 기술입니다. 번역, 요약, 감정 분석 등에 활용됩니다.",
        "컴퓨터 비전은 디지털 이미지나 비디오에서 정보를 추출하고 분석하는 기술입니다. 객체 인식, 얼굴 인식, 의료 영상 분석 등에 사용됩니다.",
        "강화학습은 에이전트가 환경과 상호작용하며 보상을 최대화하는 방향으로 학습하는 방법입니다. 게임 AI, 로봇 제어, 자율주행 등에 활용됩니다."
    ]
    # AI/ML 분야의 다양한 주제를 다루는 샘플 문서들
    # 각 문서는 특정 주제에 대한 기본적인 정의와 특징을 포함
    
    metadatas = [
        {"source": "AI 기초 교재", "topic": "인공지능 개론", "author": "김교수"},
        {"source": "ML 가이드북", "topic": "머신러닝", "author": "이박사"},
        {"source": "딥러닝 교과서", "topic": "딥러닝", "author": "박연구원"},
        {"source": "NLP 핸드북", "topic": "자연어처리", "author": "최교수"},
        {"source": "컴퓨터비전 가이드", "topic": "컴퓨터비전", "author": "정박사"},
        {"source": "강화학습 논문", "topic": "강화학습", "author": "한교수"}
    ]
    # 각 문서에 대응하는 메타데이터
    # 출처, 주제, 저자 정보를 포함하여 검색 결과의 신뢰성 제공
    
    # 문서 추가
    success = rag_system.add_documents(documents, metadatas)
    # 준비된 문서들을 시스템에 추가하고 성공 여부 확인
    
    if success:
        # 시스템 통계 출력
        stats = rag_system.get_system_stats()
        print(f"\n시스템 통계:")
        for key, value in stats.items():
            print(f"   {key}: {value}")
        # 시스템 초기화 완료 후 전체 상태 정보 출력
        
        # 테스트 질문
        print("\n테스트 질문:")
        test_result = rag_system.generate_rag_response("딥러닝과 머신러닝의 차이점은 무엇인가요?")
        print(f"답변: {test_result['answer']}")
        # 시스템이 정상 작동하는지 확인하기 위한 테스트 질문 실행
        
        # 대화형 인터페이스 실행
        rag_system.chat_interface()
        # 사용자와의 실시간 대화를 위한 인터페이스 시작
    else:
        print("문서 추가에 실패했습니다.")
        # 문서 추가 실패 시 오류 메시지 출력