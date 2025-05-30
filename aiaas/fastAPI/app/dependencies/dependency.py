from functools import lru_cache
from repositoires.repository import UserRepository
from services.user import UserService
from fastapi import Depends

@lru_cache()
def get_user_repository() -> UserRepository:
    """
    사용자 저장소 의존성 (Singleton)
    @lru_cache()로 싱글톤 패턴 구현
    애플리케이션 전체에서 하나의 인스턴스만 사용
    """
    return UserRepository()

def get_user_service(
    user_repository: UserRepository = Depends(get_user_repository)
) -> UserService:
    """
    사용자 서비스 의존성
    Repository를 주입받아 Service 생성
    의존성 체인: Router -> Service -> Repository
    """
    return UserService(user_repository)