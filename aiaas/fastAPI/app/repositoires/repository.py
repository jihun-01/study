from typing import List, Optional
from datetime import datetime
import hashlib
from models.user import User, UserCreate, UserUpdate


class UserRepository:
    """
    사용자 데이터 저장소
    """
    def __init__(self):
        self._users: List[User] = []
        self._next_id = 1

        self._add_sample_data()


    def _add_sample_data(self):
        """
        샘플 데이터 추가
        """
        sample_data = [
            UserCreate(
                name="길동",
                email="gil@example.com",
                age=30,
                password="password123"
            ),
            UserCreate(
                name="영희",
                email="young@example.com",
                age=25,
                password="password123"
            )
        ]
        
        for user_data in sample_data:
            self.create(user_data)

    def _hash_password(self, password: str) -> str:
        """비밀번호 해시 생성"""
        return hashlib.sha256(password.encode()).hexdigest()

    def create(self, user_data: UserCreate) -> User:
        """새 사용자 생성"""

        user = User(
            id=self._next_id,
            name=user_data.name,
            email=user_data.email,
            age=user_data.age,
            password_hash=self._hash_password(user_data.password),
            created_at=datetime.now(),
            updated_at=datetime.now()
        )

        self._users.append(user)
        self._next_id += 1
        return user
    
    
    def get_by_id(self, user_id: int) -> Optional[User]:
        """ID로 사용자 조회"""
        for user in self._users:
            if user.id == user_id and user.is_active:
                return user
        return None
    
    def get_by_email(self, email: str) -> Optional[User]:
        """이메일로 사용자 조회"""
        for user in self._users:
            if user.email == email and user.is_active:
                return user
        return None
    
    def get_all(self, skip: int = 0, limit: int = 100) -> List[User]:
        """모든 사용자 조회"""

        active_users = [user for user in self._users if user.is_active]
        return active_users[skip:skip+limit]
    
    def update(self, user_id: int, user_data: UserUpdate) -> Optional[User]:
        """사용자 업데이트"""
        
        user = self.get_by_id(user_id)
        if not user:
            return None
        
        
        #수정할 필드만 업데이트
        update_data = user_data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(user, field, value)

        user.updated_at = datetime.now()
        return user
    
    def delete(self, user_id: int) -> bool:
        """사용자 삭제"""

        user = self.get_by_id(user_id)
        if user:
            user.is_active = False
            user.updated_at = datetime.now()
            return True
        return False
    
    def count(self) -> int:
        """모든 사용자 수 조회"""
        return len([user for user in self._users if user.is_active])

        
