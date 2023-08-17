from typing import Annotated
from functools import lru_cache
from fastapi import Depends
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    secret_key: str
    db_table_name: str

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache()
def get_settings():
    return Settings()


AppSettings = Annotated[Settings, Depends(get_settings)]
