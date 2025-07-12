from dotenv import load_dotenv
import os

load_dotenv()  # Загружает переменные из .env
print(os.getenv('POSTGRES_USER'))
# process.exit(0)

class Config:
    DB_URL = (
        f"postgresql+asyncpg://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
        f"@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
    )

config = Config
