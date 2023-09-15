from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    # ACCESS_TOKEN_EXPIRE_MINUTES: int
    # SECRET_KEY: str
    # ALGORITHM: str
    # UPLOAD_DIR: str
    # VERIFY_OTP_API_URL = "http://localhost:8000/v1/verify_otp"

    class Config:
        env_file = ".env"


settings = Settings()
