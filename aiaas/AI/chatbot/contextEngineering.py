import os
import numpy as np
from openai import OpenAI
import json
from typing import List, Dict, Optional
import dotenv
dotenv.load_dotenv()

# FAISS 벡터 스토어와 OpenAI 임베더 import
from FAISSVectorStore import FAISSVectorStore
from Openaiembedding import OpenAIEmbedder

class RAGPromptBuilder:
    def __init__(self):
        """RAG 프롬프트 빌더 초기화"""
        self.system_prompt = """
당신은 주어진 문서들을 바탕으로 정확하고 도움이 되는 답변을 제공하는 AI 어시스턴트입니다.

지침:
1. 주어진 문서 내용만을 바탕으로 답변하세요
2. 문서에 없는 내용은 추측하지 마세요
3. 답변에 근거가 되는 문서를 명시하세요
4. 확실하지 않은 내용은 "문서에서 찾을 수 없습니다"라고 말하세요
5. 답변은 명확하고 구체적으로 작성하세요
"""
    
    def build_prompt(self, query, retrieved_docs, include_sources=True):
        """
        RAG 프롬프트 생성        
        """
        # 문서 컨텍스트 구성
        context = "=== 참고 문서 ===\n"
        for i, doc in enumerate(retrieved_docs, 1):
            if isinstance(doc, dict):
                doc_text = doc.get('document', doc.get('text', str(doc)))
                # get('document', doc.get('text', str(doc))) : 
                # 딕셔너리에서 'document' 키가 있으면 해당 값을 반환, 
                # 없으면 'text' 키가 있으면 해당 값을 반환, 없으면 str(doc) 반환
                source = doc.get('source', f'문서 {i}')
            else:
                doc_text = str(doc)
                source = f'문서 {i}'
            
            context += f"\n[{source}]\n{doc_text}\n"
        
        # 최종 프롬프트 구성
        prompt = f"""
{self.system_prompt}

{context}

=== 질문 ===
{query}

=== 답변 ===
위의 참고 문서를 바탕으로 질문에 대한 답변을 작성해주세요.
"""
        
        return prompt
    
    def build_conversational_prompt(self, query, retrieved_docs, chat_history=None):
        """
        대화형 RAG 프롬프트 생성
        """
        context = "=== 참고 문서 ===\n"
        for i, doc in enumerate(retrieved_docs, 1):
            doc_text = doc.get('document', str(doc)) if isinstance(doc, dict) else str(doc)
            # .get('document', str(doc)) : 딕셔너리에서 'document' 키가 있으면 해당 값을 반환, 없으면 str(doc) 반환
            context += f"\n[문서 {i}]\n{doc_text}\n"
        
        # 대화 기록 추가
        conversation = ""
        if chat_history:
            conversation = "\n=== 이전 대화 ===\n"
            for turn in chat_history[-3:]:  # 최근 3턴만 포함
                conversation += f"사용자: {turn.get('user', '')}\n"
                conversation += f"어시스턴트: {turn.get('assistant', '')}\n\n"
        
        prompt = f"""
{self.system_prompt}

{context}
{conversation}
=== 현재 질문 ===
{query}

=== 답변 ===
참고 문서와 이전 대화를 고려하여 답변해주세요.
"""
        
        return prompt


class VectorStore:
    """FAISS 기반 고성능 벡터 스토어"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Args:
            api_key: OpenAI API 키 (환경변수에서 자동 로드 가능)
        """
        # OpenAI 임베더 초기화
        self.embedder = OpenAIEmbedder(api_key or os.getenv('OPENAI_API_KEY'))
        
        # FAISS 스토어는 문서 추가 시점에 초기화 (차원 수 필요)
        self.faiss_store = None
        self.documents_data = []  # 원본 문서 메타데이터 저장
    
    def add_documents(self, documents: List[Dict]):
        """문서들을 FAISS 벡터 스토어에 추가"""
        print("문서 임베딩 생성 중...")
        
        # 문서 텍스트 추출
        doc_texts = []
        for doc in documents:
            text = doc.get('text', doc.get('document', str(doc)))
            # doc.get('document', str(doc)) : 딕셔너리에서 'document' 키가 있으면 해당 값을 반환, 없으면 str(doc) 반환
            # document 키가 없는데 근데
            doc_texts.append(text)
        
        # OpenAI 임베딩 생성
        embeddings_list = self.embedder.get_batch_embeddings(doc_texts)
        
        if not embeddings_list:
            print("임베딩 생성 실패!")
            return
        
        # numpy 배열로 변환
        embeddings = np.array(embeddings_list)
        
        # FAISS 스토어 초기화 (첫 번째 문서 추가 시)
        if self.faiss_store is None:
            dimension = embeddings.shape[1]  # 임베딩 차원 (보통 1536)
            # 벡터 디비와 문서 데이터 차원 맞춰주기
            self.faiss_store = FAISSVectorStore(dimension)
            print(f"FAISS 인덱스 초기화 완료 (차원: {dimension})")
        
        # 문서를 FAISS에 추가
        self.faiss_store.add_documents(doc_texts, embeddings)
        
        # 메타데이터 저장
        self.documents_data.extend(documents)
        
        print(f"{len(documents)}개 문서가 FAISS 벡터 스토어에 추가되었습니다.")
    
    def search(self, query: str, top_k: int = 3) -> List[Dict]:
        """FAISS 기반 의미적 검색"""
        print(f"\n검색 쿼리: '{query}'")
        
        if self.faiss_store is None:
            print("FAISS 인덱스가 초기화되지 않았습니다!")
            return []
        
        print(f"총 문서 수: {len(self.documents_data)}")
        
        # 1. 쿼리 임베딩 생성
        print("쿼리 임베딩 생성 중...")
        query_embedding_list = self.embedder.get_embedding(query)
        
        if not query_embedding_list:
            print("쿼리 임베딩 생성 실패!")
            return []
        
        # 2. FAISS 검색 실행
        query_embedding = np.array(query_embedding_list)
        faiss_results = self.faiss_store.search(query_embedding, top_k=top_k)
        
        print(f"FAISS 검색 완료: {len(faiss_results)}개 결과")
        
        # 3. 결과를 기존 형식에 맞게 변환
        results = []
        for faiss_result in faiss_results:
            # FAISS 결과에서 인덱스 추출
            doc_index = faiss_result['index']
            
            if doc_index < len(self.documents_data):
                # 원본 문서 메타데이터 가져오기
                original_doc = self.documents_data[doc_index].copy()
                # copy() : 딕셔너리를 복사하여 새로운 딕셔너리를 생성
                original_doc['score'] = faiss_result['score']
                # score : 문서와 쿼리의 유사도
                results.append(original_doc)
                
                print(f"선택된 문서: {original_doc.get('title', '제목없음')} "
                      f"(유사도: {faiss_result['score']:.3f})")
        
        print(f"반환할 문서 수: {len(results)}")
        return results


class RAGChatbot:
    """OpenAI 기반 RAG 챗봇"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        RAG 챗봇 초기화
        """
        # OpenAI 클라이언트 초기화
        self.client = OpenAI(api_key=api_key or os.getenv('OPENAI_API_KEY'))
        
        # 컴포넌트 초기화
        self.prompt_builder = RAGPromptBuilder()
        self.vector_store = VectorStore(api_key)  # API 키 전달
        self.chat_history = []
    
    def load_documents(self, documents: List[Dict]):
        """지식 베이스 문서 로드"""
        self.vector_store.add_documents(documents)
    
    def chat(self, query: str, use_history: bool = True) -> str:
        """
        사용자 질문에 대한 답변 생성
        """
        try:
            # 1. 관련 문서 검색
            print(f"\n사용자 질문: '{query}'")
            retrieved_docs = self.vector_store.search(query, top_k=3)
            
            print(f"검색된 문서 수: {len(retrieved_docs)}")
            
            if not retrieved_docs:
                print("검색된 문서가 없습니다!")
                return "죄송합니다. 관련된 정보를 찾을 수 없습니다."
            
            # 2. 프롬프트 생성
            if use_history and self.chat_history:
                prompt = self.prompt_builder.build_conversational_prompt(
                    query, retrieved_docs, self.chat_history
                )
            else:
                prompt = self.prompt_builder.build_prompt(query, retrieved_docs)
            
            # 3. OpenAI API 호출
            response = self.client.chat.completions.create(
                model="gpt-4.1-nano",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                # temperature : 1에 가까울수록 모델은 더 창의적인 답변을 생성
                # 0에 가까울수록 모델은 더 정확한 답변을 생성
                max_tokens=1000
                # max_tokens : 생성할 토큰의 최대 개수
            )
            
            answer = response.choices[0].message.content
            
            # 4. 대화 기록 업데이트
            self.chat_history.append({
                "user": query,
                "assistant": answer,
                "retrieved_docs": len(retrieved_docs)
            })
            
            return answer
            
        except Exception as e:
            return f"오류가 발생했습니다: {str(e)}"
    
    def get_chat_history(self) -> List[Dict]:
        """대화 기록 반환"""
        return self.chat_history
    
    def clear_history(self):
        """대화 기록 초기화"""
        self.chat_history = []


# 실제 사용 예제
if __name__ == "__main__":
    # 1. 샘플 문서 데이터
    sample_documents = [
        {
            'text': '인공지능(AI)은 인간의 지능을 모방하는 컴퓨터 시스템입니다. AI는 학습, 추론, 문제해결 능력을 갖추고 있습니다.',
            'source': 'AI 기초 교재',
            'title': 'AI 개념'
        },
        {
            'text': '머신러닝은 AI의 한 분야로, 데이터로부터 패턴을 학습하여 예측을 수행합니다. 지도학습, 비지도학습, 강화학습으로 나뉩니다.',
            'source': 'ML 가이드북',
            'title': '머신러닝 기초'
        },
        {
            'text': '딥러닝은 인공신경망을 이용한 머신러닝 기법입니다. 이미지 인식, 자연어 처리 등에서 뛰어난 성능을 보입니다.',
            'source': 'DL 논문',
            'title': '딥러닝 개념'
        },
        {
            'text': 'ChatGPT는 OpenAI에서 개발한 대화형 AI 모델입니다. GPT 아키텍처를 기반으로 하며, 자연스러운 대화가 가능합니다.',
            'source': 'OpenAI 블로그',
            'title': 'ChatGPT 소개'
        },
        {
            'text': 'RAG(Retrieval-Augmented Generation)는 외부 지식을 검색하여 답변 생성에 활용하는 기법입니다.',
            'source': 'RAG 연구논문',
            'title': 'RAG 기법'
        }
    ]
    
    # 2. RAG 챗봇 초기화 (API 키 필요)
    # 환경변수 OPENAI_API_KEY 설정 또는 직접 전달
    
    chatbot = RAGChatbot()  # API 키가 환경변수에 있어야 함
    
    # 3. 문서 로드
    chatbot.load_documents(sample_documents)
    
    # 4. 대화 시뮬레이션
    print("=== RAG 챗봇 테스트 ===\n")
    
    questions = [
        "인공지능이 뭐야?",
        "머신러닝과 딥러닝의 차이는?",
        "RAG가 뭔지 설명해줄래?",
        "ChatGPT에 대해 알려줘"
    ]
    
    for question in questions:
        print(f"질문: {question}")
        answer = chatbot.chat(question)
        print(f"답변: {answer}\n")

 