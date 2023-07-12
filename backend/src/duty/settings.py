import pathlib
from functools import cache

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = pathlib.Path(__file__).parent.parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="DUTY_BOT_", env_file=BASE_DIR / ".env")
    pg_dsn: PostgresDsn
    db_session_echo: bool = False


@cache
def get_settings() -> Settings:
    return Settings()
