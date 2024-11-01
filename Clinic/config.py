from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    USER: str
    PASSWORD: str
    HOST_NAME: str
    DB_NAME: str
    JWT_SECRET_KEY: str
    JWT_TOKEN_LOCATION: str

    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()