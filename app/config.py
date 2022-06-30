from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = ""
    secret: str = None
    img_key: str = None
    mega_email: str = None
    mega_psw: str = None

    class Config:
        env_file = ".env"
