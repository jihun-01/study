from openai import OpenAI
import os
import dotenv
dotenv.load_dotenv()


class OpenAIChatbot:
    def __init__(self, api_key:str, model:str='gpt-4.1-nano'):

        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.conversation_history = []
        self.system_message = {
            'role': 'system',
            'content': '당신은 카페 주문을 받는 친절한 직원입니다. 메뉴 추천과 주문 처리를 도와주세요.'
        }
    
    def set_system_prompt(self, prompt:str):
        self.system_message['content'] = prompt
        
    def add_message(self, role:str, content:str):
        self.conversation_history.append({
            'role': role,
            'content': content
        })
    # 대화 기록 추가
    def get_response(self, user_message:str):
        
        self.add_message('user', user_message)
        
        messages = [self.system_message] + self.conversation_history

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=1000,
                temperature=0.7,
                presence_penalty=0.6,
                frequency_penalty=0.0
            )

            
            
            assistant_message = response.choices[0].message.content

            self.add_message('assistant', assistant_message)

            return assistant_message
        
        except Exception as e:
            print(f"Error: {e}")
            return "오류가 발생했습니다. 다시 시도해주세요."
    def clear_history(self):
        self.conversation_history = []

if __name__ == '__main__':
    # chatbot 선언
    
    api_key = os.getenv("OPENAI_API_KEY")
    chatbot = OpenAIChatbot(api_key)

    chatbot.set_system_prompt("당신은 카페 주문을 받는 친절한 직원입니다. 메뉴 추천과 주문 처리를 도와주세요.")

    # 첫 번째 사용자 입력과 챗봇 응답
    user_input = "안녕하세요, 추천 메뉴가 있나요?"
    response = chatbot.get_response(user_input)
    print(f"챗봇: {response}")

    # 연속적인 대화 - 이전 맥락이 유지됨
    user_input = "달지 않은 음료를 원해요"
    response = chatbot.get_response(user_input)
    print(f"챗봇: {response}")