from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET: str
    REDIS_HOST: str
    REDIS_PORT: int

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


Config = DatabaseSettings()
