from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )

    uvicorn_host: str = Field("localhost", alias="UVICORN_HOST")
    uvicorn_port: int = Field(8000, alias="UVICORN_PORT")

    app_debug: bool = Field(False, alias="APP_DEBUG")


@lru_cache()
def get_settings() -> Settings:
    return Settings()
