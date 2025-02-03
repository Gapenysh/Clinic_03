from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    USER: str
    PASSWORD: str
    HOST_NAME: str
    DB_NAME: str
    EASYCLINIC_API_URL: str
    EASYCLINIC_API_KEY: str
    PASSWORD_BY_MAIL: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()