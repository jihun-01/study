from pydantic import BaseModel
from typing import Optional

class MessageResponse(BaseModel):
    """일반적인 메시지 응답 모델"""
    message: str
    success: bool = True

class ErrorResponse(BaseModel):
    """오류 응답 모델"""
    message: str
    error_code: Optional[str] = None
    success: bool = False

class PaginatedResponse(BaseModel):
    """페이지네이션 응답 모델"""
    items: list
    total: int
    page: int
    size: int
    has_next: bool
    has_prev: bool



