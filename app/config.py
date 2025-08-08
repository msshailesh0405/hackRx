from pydantic import BaseSettings

class Settings(BaseSettings):
    TEAM_TOKEN: str = "dev-token"  # Change in .env for real token

    class Config:
        env_file = ".env"

settings = Settings()
