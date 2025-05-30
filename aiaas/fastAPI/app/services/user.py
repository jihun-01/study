from typing import Optional
from models.user import User, UserCreate, UserUpdate, UserResponse
from models.base import PaginatedResponse
from repositoires.repository import UserRepository

class UserService:
    """
    사용자 관련 비즈니스 로직 처리
    """
    def __init__(self, user_repository: UserRepository):
        """
        UserService 초기화
        """
        self.user_repository = user_repository

    def create_user(self, user_data: UserCreate) -> UserResponse:
        """
        새 사용자 생성
        """
        existing_user = self.user_repository.get_by_email(user_data.email)
        #이메일 중복 체크
        if existing_user:
            raise ValueError(f"{user_data.email}은 이미 존재하는 이메일입니다.")
        
        #나이 체크
        if user_data.age < 14:
            raise ValueError("14세 미만의 사용자는 회원가입을 할 수 없습니다.")

        if not user_data.name.strip():
            raise ValueError("이름은 공백으로 입력할 수 없습니다.")

        user = self.user_repository.create(user_data)

        return UserResponse(
            id=user.id,
            name=user.name,
            email=user.email,
            age=user.age,
            created_at=user.created_at,
            updated_at=user.updated_at
        )
        
    def get_user(self, user_id: int) -> Optional[UserResponse]:
        """
        사용자 조회
        """
        user = self.user_repository.get_by_id(user_id)
        if not user:
            return None
        
        return UserResponse(
            id=user.id,
            name=user.name,
            email=user.email,
            age=user.age,
            created_at=user.created_at,
            updated_at=user.updated_at
        )
        
    def get_users(self, skip: int = 0 , limit: int = 10) -> PaginatedResponse:
        """
        사용자 목록 조회
        """
        users = self.user_repository.get_all(skip, limit)
        total = self.user_repository.count()

        user_responses = [
            UserResponse(
                id=user.id,
                name=user.name,
                email=user.email,
                age=user.age,
                created_at=user.created_at,
                updated_at=user.updated_at
            )
            for user in users
        ]

        page = (skip // limit) + 1 if limit > 0 else 1
        has_next = (skip + limit) < total
        has_prev = skip > 0

        return PaginatedResponse(
            items=user_responses,
            total=total,
            page=page,
            size=len(user_responses),
            has_next=has_next,
            has_prev=has_prev
        )
    
    def update_user(self, user_id: int, user_data: UserUpdate) -> UserResponse:
        """
        사용자 정보 수정
        """
        existing_user = self.user_repository.get_by_id(user_id)
        if not existing_user:
            return None
        
        #이메일 중복 체크
        if user_data.email:
            email_user = self.user_repository.get_by_email(user_data.email)
            if email_user and email_user.id != user_id:
                raise ValueError(f"{user_data.email}은 이미 사용중인 이메일입니다.")
            
        if user_data.age is not None and user_data.age < 14:
           raise ValueError("14세 미만으로 변경할 수 없습니다.")

        # 사용자 정보 수정
        updated_user = self.user_repository.update(user_id, user_data)
        if not updated_user:
            return None

        return UserResponse(
            id=updated_user.id,
            name=updated_user.name,
            email=updated_user.email,
            age=updated_user.age,
            created_at=updated_user.created_at,
            updated_at=updated_user.updated_at
        )

    def delete_user(self, user_id: int) -> bool:
        """
        사용자 삭제
        """
        return self.user_repository.delete(user_id)
            
        
