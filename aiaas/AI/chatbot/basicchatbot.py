class BasicChatbot:
    def __init__(self):
        # 의도 정의
        self.intents = {
            'greeting': ["안녕"," hi", "hello", "반가워"],
            'weather': ["날씨", "weather", "비","맑아"],
            'goodbye': ["안녕히", "bye", "goodbye", "잘가"]
        }
        # 응답 정의
        self.responses = {
            'greeting': ["안녕하세요! 무엇을 도와드릴까요?", "반갑습니다!"],
            'weather': ["날씨 정보를 조회하겠습니다.", "어느 지역의 날씨를 알고 싶으신가요?"],
            'goodbye': ["안녕히 가세요!","다음에 또 만나요!"],
            'default': ["죄송합니다. 이해할 수 없는 메시지입니다."]
        }
    
    # 의도 분류
    def classify_intent(self, user_input):
        user_input = user_input.lower()
        for intent, keywords in self.intents.items():
            for keyword in keywords:
                if keyword in user_input:
                    return intent
        return 'default'
    
    # 응답 생성
    def generate_response(self, intent):
        import random
        responses = self.responses.get(intent, self.responses['default'])
        return random.choice(responses)
    
    # 대화 시작
    def chat(self, user_input):
        intent = self.classify_intent(user_input)
        response = self.generate_response(intent)
        return response
    
if __name__ == '__main__':
    bot = BasicChatbot()
    print(bot.chat("안녕하세요"))
    print(bot.chat("오늘 날씨"))
    print(bot.chat("잘가"))