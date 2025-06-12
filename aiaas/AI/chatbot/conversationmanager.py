from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
import json
from datetime import datetime
import uuid
from OpenAiChatbot import OpenAIChatbot
import os
import dotenv
from EntityExtractor import EntityExtractor
#env 파일 로드
dotenv.load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

@dataclass
class DialogState:
    session_id: str

    entities: Dict[str, Any] = field(default_factory=dict)
    context_stack: List[Dict] = field(default_factory=list)
    user_profile: Dict[str, Any] = field(default_factory=dict)
    conversation_history: List[dict] = field(default_factory=list)
    last_updated: datetime = field(default_factory=datetime.now)

    def add_turn(self, user_input: str, bot_response: str, entities: Dict = None):

        turn = {
            "timestamp": datetime.now().isoformat(),
            "user_input": user_input,
            "bot_response": bot_response,
            "entities": entities or {}
        }

        self.conversation_history.append(turn)

        if entities:
            self.entities.update(entities)

        self.last_updated = datetime.now()

    def get_context(self, turns: int = 3) -> List[dict]:

        return self.conversation_history[-turns:] if self.conversation_history else []
    
    def clear_context(self):
        self.conversation_history = []
        self.entities = {}
        self.context_stack = []

class ConversationManager:

    def __init__(self):
        self.sessions: Dict[str, DialogState] = {}
        self.entity_extractor = EntityExtractor()
    
    def create_session(self, user_id: str =None) -> str:

        session_id = user_id or str(uuid.uuid4())
        self.sessions[session_id] = DialogState(session_id=session_id)
        return session_id
    
    def get_session(self, session_id: str) -> Optional[DialogState]:
        return self.sessions.get(session_id)
    
    def process_message(self, session_id: str, user_input: str, chatbot) -> str:

        if session_id not in self.sessions:
            self.create_session(session_id)
        
        dialog_state = self.sessions[session_id]

        entities = self.entity_extractor.extract_entities(user_input)
        
        entity_dict = {ent['text']: ent['label'] for ent in entities}

        context_prompt = self._build_context_prompt(dialog_state, user_input)

        response = chatbot.get_response(context_prompt)

        dialog_state.add_turn(
            user_input=user_input,
            bot_response=response,
            entities=entity_dict
        )

        return response
    
    def _build_context_prompt(self, dialog_state: DialogState, current_input: str) -> str:

        context_info = []

        recent_context = dialog_state.get_context(turns=3)
        if recent_context:
            context_info.append("최근 대화 내용:")
            for turn in recent_context:
                context_info.append(f"사용자: {turn['user_input']}")
                context_info.append(f"봇: {turn['bot_response']}")

        if dialog_state.entities:
            context_info.append(f"기억된 정보: {dialog_state.entities}")
        
        if dialog_state.user_profile:
            context_info.append(f"사용자 정보: {dialog_state.user_profile}")
        
        context_info.append(f"현재 질문: {current_input}")

        return "\n".join(context_info)
    
    def update_user_profile(self, session_id: str, profile_data: Dict):
        if session_id in self.sessions:
            self.sessions[session_id].user_profile.update(profile_data)

    def get_conversation_summary(self, session_id: str) -> str:

        dialog_state = self.sessions.get(session_id)
        if not dialog_state or not dialog_state.conversation_history:
            return "대화 내역이 없습니다."
         
        summary_parts = []
        summary_parts.append(f"세션 ID: {session_id}")
        summary_parts.append(f"대화 턴 수: {len(dialog_state.conversation_history)}")
        summary_parts.append(f"추출된 개체: {dialog_state.entities}")

        return "\n".join(summary_parts)
    

if __name__ == "__main__":
    conv_manager = ConversationManager()
    chatbot = OpenAIChatbot(api_key)
    chatbot.set_system_prompt("당신은 친절한 비서입니다.")

    session_id = conv_manager.create_session("user154")

    response1 = conv_manager.process_message(session_id, "안녕하세요", chatbot)
    print(f'봇1: {response1}')

    # 두 번째 메시지 처리 - 사용자 이름 정보 제공 및 개체 추출

    # 사용자 프로필 업데이트
    conv_manager.update_user_profile(session_id, {"name": "김철수", "age": 30})
    # 추출된 정보를 체계적으로 사용자 프로필에 저장 - 개인화 서비스 기반 마련

    response3 = conv_manager.process_message(session_id, "아까 제가 뭐라고 했죠?", chatbot)
    print(f"봇3: {response3}")
    # 세 번째 메시지 처리 - 이전 대화 참조 질문으로 컨텍스트 관리 기능 테스트

    response4 = conv_manager.process_message(session_id, "제 나이에 맞는 취미를 추천해주세요", chatbot)
    print(f"봇4: {response4}")

    # 대화 요약
    summary = conv_manager.get_conversation_summary(session_id)
    print(f"대화 요약:\n{summary}")
    # 전체 대화 세션의 요약 정보 출력 - 관리 및 분석 목적
