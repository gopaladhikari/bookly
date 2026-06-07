from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class DatabaseSettings(BaseSettings):
    DATABASE_URL: str = Field(default=...)
    JWT_SECRET: str = Field(default=...)

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


Config = DatabaseSettings()
