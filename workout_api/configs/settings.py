from pydantic import Field
from pydantic_settings import BaseSettings

#Configuração da API
class Settings(BaseSettings):
    DB_URL: str = Field(default='postgresql+asyncpg://postgres:teste@localhost/workout')
    
settings = Settings()