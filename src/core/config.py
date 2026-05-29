from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class DatabaseSettings(BaseSettings):
    DB_URI: str = Field(default=...)

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


Config = DatabaseSettings()
