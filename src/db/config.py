from pydantic_settings import BaseSettings

# Define settings for database configuration using Pydantic
class Settings(BaseSettings):
  DATABASE_URL: str
  class Config:
    env_file = ".env"

# Initialize settings
settings = Settings()