# from fastapi import FastAPI, status , HTTPException, Depends
# from pydantic import BaseModel, Field, field_validator, ValidationError
# from typing import Optional
# from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
# import re
# from fastapi.exceptions import RequestValidationError
# from fastapi.responses import JSONResponse

# security = HTTPBearer()
# app = FastAPI()

# @app.get("users", dependencies=[Depends(security)])
# def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):

#     token = credentials.credentials
#     print(token)

#     return {"message": token}

# class UserCreate(BaseModel):
#     name:str
#     age:int
#     price:float


# user1 = UserCreate(
#     name="asda",
#     age=10,
#     price=15.321
# )

# @app.post("/users")
# def create_user(user:UserCreate):
#     return user




# class UserCreate(BaseModel):
#     username:str
#     password:str
#     confirm_password:str
#     email:str
#     age:int


# @field_validator("username")
# @classmethod
# def username_must_be_alphanumeric(cls, v):
#     if not re.match(r'^[a-zA-Z0-9]+$', v):
#         raise ValueError("사용자 명은 영문자와 숫자만 포함할 수 있습니다.")
#     return v

# @field_validator("email")
# @classmethod
# def email_must_be_valid(cls, v):
#     if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', v):
#         raise ValueError("이메일 형식이 올바르지 않습니다.")
#     return v
# try:
#     user = UserCreate(
#         username="",              # 빈 문자열
#         age="not_a_number",   # 숫자가 아님
#         grades=["A", "B"],    # 문자열(숫자여야 함)
#         email="invalid_email" # 잘못된 이메일 형식
#     )
# except ValidationError as e:
#     print("검증 에러 발생:")
#     for error in e.errors():
#         print(f" - 필드: {error['loc']}")
#         print(f"   메시지: {error['msg']}")
#         print(f"   타입: {error['type']}")
#         print(f"   입력값: {error['input']}")
#         print()

# class StudentCreate(BaseModel):
#     name:str
#     age:int
#     grades:list[float]
#     email:str

# @app.exception_handler(RequestValidationError)
# def validation_exception_handler(request, exc):
#     return JSONResponse(
#         status_code=422,
#         content={
#             "message": "입력 데이터 검증에 실패했습니다",
#             "details": [
#                 {
#                     "field": " -> ".join(str(loc) for loc in error['loc']),  # Loc : 검증 실패한 필드의 경로
#                     "message": error['msg'],
#                     "input": error.get('input')
#                 }
#                 for error in exc.errors()
#             ]
#         }
#     )

# @app.post("/students")
# def create_student(student:StudentCreate):
#     return f"{student.name} 등록 완료"


# class Address(BaseModel):
#     street: str
#     city: str
#     postal_code: str
#     country: str = "대한민국"

# class Customer(BaseModel):
#     name: str
#     email: str
#     phone: str
#     address: Address

# class OrderItem(BaseModel):
#     product_name: str
#     quantity: int
#     unit_price: float

#     @property
#     def total_price(self) -> float:
#         return self.quantity * self.unit_price

# class Order(BaseModel):
#     order_id: str
#     customer: Customer
#     items: list[OrderItem]
#     order_date: datetime
#     status: str = "pending"
#     notes: Optional[str] = None

#     @property
#     def total_amount(self) -> float:
#         return sum(item.total_price for item in self.items)


# order_data = {
#     "order_id": "ORD-2024-001",
#     "customer": {
#         "name": "김철수",
#         "email": "kim@example.com",
#         "phone": "010-1234-5678",
#         "address": {
#             "street": "강남대로 123",
#             "city": "서울",
#             "postal_code": "06234"
#         }
#     },
#     "items": [
#         {
#             "product_name": "노트북",
#             "quantity": 1,
#             "unit_price": 1500000
#         },
#         {
#             "product_name": "마우스",
#             "quantity": 2,
#             "unit_price": 25000
#         }
#     ],
#     "order_date": "2024-01-01T10:00:00"
# }

# order = Order(**order_data)
# print(order.total_amount)


#####################################################

# from fastapi import FastAPI
# from pydantic import BaseModel, model_validator
# from typing import Optional

# app = FastAPI()

# class ShippingInfo(BaseModel):
#     method: str  # "pickup", "delivery", "express"
#     address: Optional[str] = None
#     pickup_store: Optional[str] = None
#     express_time: Optional[str] = None

#     @model_validator(mode='after')
#     def validate_shipping_method(self):
#         method = self.method

#         if method == "delivery":
#             if not self.address:
#                 raise ValueError('배송 방법이 "delivery"인 경우 주소가 필요합니다.')

#         elif method == "pickup":
#             if not self.pickup_store:
#                 raise ValueError('배송 방법이 "pickup"인 경우 픽업 매장이 필요합니다.')

#         elif method == "express":
#             if not self.address:
#                 raise ValueError('배송 방법이 "express"인 경우 주소가 필요합니다.')
#             if not self.express_time:
#                 raise ValueError('배송 방법이 "express"인 경우 배송 시간이 필요합니다.')

#         return self


# delivery_info = ShippingInfo(
#     method="delivery",
#     address="서울시 강남구 테헤란로 123"
# )

# pickup_info = ShippingInfo(
#     method="pickup",
#     pickup_store="강남점"
# )

# express_info = ShippingInfo(
#     method="express",
#     address="서울시 강남구 테헤란로 123",
#     express_time="2024-01-01 14:00"
# )


#####################################################
#응답
# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse, PlainTextResponse, FileResponse
# import json
# import os

# app = FastAPI()

# # JSON 응답 (기본)
# @app.get("/api/data")
# async def get_json_data():
#     return {"message": "안녕하세요", "status": "success"}

# # HTML 응답
# @app.get("/html", response_class=HTMLResponse)
# async def get_html():
#     return """
#     <html>
#         <head><title>FastAPI HTML</title></head>
#         <body>
#             <h1>안녕하세요, FastAPI!</h1>
#             <p>이것은 HTML 응답입니다.</p>
#         </body>
#     </html>
#     """

# # 텍스트 응답
# @app.get("/text", response_class=PlainTextResponse)
# async def get_text():
#     return "이것은 단순한 텍스트 응답입니다."

# # 파일 응답
# @app.get("/download")
# async def download_file():
#     # 예제 파일이 없으면 생성
#     file_path = "example.txt"
#     if not os.path.exists(file_path):
#         with open(file_path, "w", encoding="utf-8") as f:
#             f.write("예제 파일입니다.\n")
#             f.write("파일 다운로드 테스트.\n")

#     return FileResponse(
#         path=file_path,
#         filename="파일.txt",
#         media_type="text/plain"
#     )


# #커스텀 응답

# from fastapi import FastAPI, status, HTTPException
# from fastapi.responses import JSONResponse


# app = FastAPI()

# @app.get("/success", status_code=status.HTTP_200_OK)
# def get_success():
#     return {"message": "성공"}

# @app.post("/create", status_code=status.HTTP_201_CREATED)
# def create_item():
#     return {"message": "생성 완료"}

# @app.delete("/delete/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_item(item_id: int):
#     return

# @app.get('bad_request')
# def bad_request_example():
#     return HTTPException(
#         status_code=status.HTTP_400_BAD_REQUEST,
#         detail="잘못된 요청입니다."
#     )


#####################################################
