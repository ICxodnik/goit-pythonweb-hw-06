from dotenv import load_dotenv
import os

load_dotenv()  # Загружает переменные из .env

class Config:
    DB_URL = (
        f"postgresql+asyncpg://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
        f"@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
    )

config = Config
