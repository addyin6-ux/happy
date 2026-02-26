<<<<<<< HEAD
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "LoanMarketplace"
    ENV: str = os.getenv("ENV", "development")
    JWT_SECRET: str = os.getenv("JWT_SECRET", "change_this_secret")
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60 * 24 * 7
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./app.db")
    SMS_PROVIDER_API_KEY: str = os.getenv("SMS_PROVIDER_API_KEY", "")
    AES_KEY: str = os.getenv("AES_KEY", "32_byte_aes_key_here_1234567890")
    CIBIL_API_URL: str = os.getenv("CIBIL_API_URL", "")
    AADHAAR_ESIGN_URL: str = os.getenv("AADHAAR_ESIGN_URL", "")
    PAYMENT_GATEWAY_URL: str = os.getenv("PAYMENT_GATEWAY_URL", "")

    class Config:
        env_file = ".env"
        extra = "allow"   # ✅ this line lets uppercase fields pass

def SettingsFactory():
    return Settings()

=======
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "LoanMarketplace"
    ENV: str = os.getenv("ENV", "development")
    JWT_SECRET: str = os.getenv("JWT_SECRET", "change_this_secret")
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60 * 24 * 7
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./app.db")
    SMS_PROVIDER_API_KEY: str = os.getenv("SMS_PROVIDER_API_KEY", "")
    AES_KEY: str = os.getenv("AES_KEY", "32_byte_aes_key_here_1234567890")
    CIBIL_API_URL: str = os.getenv("CIBIL_API_URL", "")
    AADHAAR_ESIGN_URL: str = os.getenv("AADHAAR_ESIGN_URL", "")
    PAYMENT_GATEWAY_URL: str = os.getenv("PAYMENT_GATEWAY_URL", "")

    class Config:
        env_file = ".env"
        extra = "allow"   # ✅ this line fixes the validation error

def SettingsFactory():
    return Settings()
>>>>>>> b9b74cb (Save all my latest work from Codespaces)
