import fastapi
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/menu")
def get_menu():
    return {"메뉴" : ["아메리카노","라떼","카푸치노"]}

@app.post("/orders")
def create_order(order_data: dict):
    return {"메시지": "주문 완료", "주문 번호": 123}

@app.get("/user/{user_id}")
def get_user(user_id: int):
    if user_id <= 0:
        return {"error": "유효하지 않은 사용자 ID입니다."}
    if user_id == 999:
        return {"message": "special user."}

    return {"user_id": user_id, "name": "홍길동", "email": "hong@example.com"}

@app.get("/cafe/{menu_item}/{item_name}")
def get_cafe_item(menu_item: str, item_name: str):
    return {
        "메뉴 항목": menu_item, 
        "항목 이름": item_name,
        "설명": f"{menu_item}의 {item_name}입니다."
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


