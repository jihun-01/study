import os
import json
from datetime import datetime
from openai import OpenAI
import dotenv
from OpenAiChatbot import OpenAIChatbot
dotenv.load_dotenv()

class AdvancedChatbot(OpenAIChatbot):

    def __init__(self, api_key:str, model:str='gpt-4.1-nano'):
        super().__init__(api_key, model)
        self.available_functions = {
            'get_weather': self.get_weather,
            'calculate' : self.calculate,
            'get_time' : self.get_time
        }
    
    def get_weather(self, location:str) -> str:
        """ 예시 함수: 날씨 정보 반환"""
        weather_data = {
            "서울": "맑음, 32도",
            "부산": "흐림, 28도",
            "대구": "비, 25도",
        }
        return weather_data.get(location, "해당 지역의 날씨 정보를 찾을 수 없습니다.")
    
    def calculate(self, expression:str) -> str:
        """ 예시 함수: 수식 계산"""
        try:
            result = eval(expression) #실제 환경에서는 보안상 문제가 있을 수 있음
            return f"{expression} = {result}"

        except:
            return "계산할 수 없는 수식입니다."
    
    def get_time(self) -> str:
        """ 예시 함수: 현재 시간 반환"""
        return datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분 %S초")
    
    def get_function_response(self, user_message:str) -> str:

        tools = [
            {
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "description": "지역의 날씨 정보를 반환합니다.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "날씨를 조회할 지역 이름"
                            }
                        },
                        "required": ["location"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "calculate",
                    "description": "수식을 계산합니다.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "expression": {
                                "type": "string",
                                "description": "계산할 수식"
                            }
                        },
                        "required": ["expression"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "get_time",
                    "description": "현재 시간을 반환합니다.",
                    "parameters": {
                        "type": "object",
                        "properties": {}
                    }
                }
            }
        ]

        self.add_message('user', user_message)
        messages = [self.system_message] + self.conversation_history

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=tools,
                tool_choice="auto"
            )
        
            message = response.choices[0].message

            if message.tool_calls:
                tool_call = message.tool_calls[0]
                function_name = tool_call.function.name
                arguments = json.loads(tool_call.function.arguments)

                if function_name in self.available_functions:
                    function_response = self.available_functions[function_name](**arguments)
                    self.add_message('assistant','')
                    self.conversation_history[-1]['tool_calls'] = message.tool_calls

                    self.conversation_history.append({
                        'role': 'tool',
                        'content': function_response,
                        'tool_call_id': tool_call.id
                    })

                    final_response = self.client.chat.completions.create(
                        model=self.model,
                        messages=[self.system_message] + self.conversation_history
                    )

                    final_message = final_response.choices[0].message.content
                    self.add_message('assistant', final_message)

                    return final_message
                
                else:
                    assistant_message = message.content
                    self.add_message('assistant', assistant_message)
                    return assistant_message
                
        except Exception as e:
            return f"오류가 발생했습니다. 다시 시도해주세요. : {str(e)}"
        

if __name__ == '__main__':
    api_key = os.getenv("OPENAI_API_KEY")
    
    advanced_bot = AdvancedChatbot(api_key)
    advanced_bot.set_system_prompt("당신은 친절한 비서입니다. 함수 호출을 통해 날씨 정보, 계산 결과, 현재 시간을 조회할 수 있습니다.")

    # 날씨 조회 테스트
    response = advanced_bot.get_function_response("서울 날씨 어때?")
    print(f"봇: {response}")

    # 계산 테스트
    response = advanced_bot.get_function_response("25 곱하기 4는 얼마야?")
    print(f"봇: {response}")

    # 시간 조회 테스트
    response = advanced_bot.get_function_response("지금 몇 시야?")
    print(f"봇: {response}")
            
 
            
