from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    """ 유저 기본 모델 """
    name : str = Field(..., min_length=2, max_length=40, description="사용자 이름")
    email : EmailStr = Field(..., description="이메일 주소")
    age: int = Field(..., ge=0, le=150, description="사용자 나이")

class UserCreate(UserBase):
    """
    사용자 생성 모델
    - 새 사용자 등록시 사용
    - 비밀번호 필드 추가
    """
    password : str = Field(..., min_length=8, description="비밀번호 (최소 8자 이상)")

class UserUpdate(UserBase):
    """
    사용자 업데이트 모델
    - 기존 사용자 정보 업데이트시 사용
    """
    name : Optional[str] = Field(None, min_length=2, max_length=40)
    email : Optional[EmailStr] = Field(None)
    age : Optional[int] = Field(None, ge=0, le=150)

class UserResponse(UserBase):
    """
    사용자 응답 모델
    - API 응답에서 사용
    - 비밀번호 필드 제외
    """
    id : int = Field(..., description="사용자 ID")
    created_at : datetime = Field(..., description="생성 일시")
    updated_at : datetime = Field(..., description="수정 일시")

class User(UserBase):
    """
    내부 사용자 모델
    - 모든 필드 포함
    - 실제 데이터 저장 시 사용
    """
    id : Optional[int] = None
    password_hash : str = Field(..., description="비밀번호 해시")
    created_at : datetime = Field(default_factory=datetime.now)
    updated_at : datetime = Field(default_factory=datetime.now)
    is_active : bool = Field(default=True, description="활성 상태")


