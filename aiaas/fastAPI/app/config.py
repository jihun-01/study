import os
from dotenv import load_dotenv
load_dotenv()
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    애플리케이션 설정 클래스
    - .env 파일에서 설정 값을 로드
    - 환경 변수 관리 및 애플리케이션 설정 관리
    """

    PROJECT_NAME: str = os.getenv("PROJECT_NAME")
    VERSION: str = os.getenv("VERSION")
    DEBUG: bool = os.getenv("DEBUG")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT")
    # API 설정
    API_PREFIX: str = os.getenv("API_PREFIX")
    #보안 설정
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    # 데이터베이스 설정
    DATABASE_URL: str = os.getenv("DATABASE_URL")

settings = Settings()
