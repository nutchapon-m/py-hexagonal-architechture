from pydantic_settings import BaseSettings, SettingsConfigDict

class Env(BaseSettings):
    SERVER_MODE: str | None
    SERVER_PORT: int | None
    model_config = SettingsConfigDict(env_file=".env")
    
env = Env()