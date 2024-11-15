import multiprocessing
from typing import Literal, Union

from pydantic import AnyHttpUrl, field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # API Settings
    APP_NAME: str = "Catan Spotter"
    API_PREFIX: str = "/api/v1"
    DEBUG: bool = False

    # Server Settings
    HOST: str = "0.0.0.0"
    PORT: int = 9999
    RELOAD: bool = False  # For development auto-reload
    WORKERS: int = multiprocessing.cpu_count()

    # CORS Settings
    ALLOWED_ORIGINS: list[Union[AnyHttpUrl] | Literal["*"]] = ["*"]

    # Validators
    @field_validator("ALLOWED_ORIGINS", mode="before")
    @classmethod
    def assemble_cors_origins(cls, v: str | list[str]) -> list[str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, list):
            return v
        raise ValueError(v)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()
