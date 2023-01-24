import os


DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
CHROME_DRIVER_URL = os.getenv("CHROME_DRIVER_URL")
CURRENCY_CONVERTER_URL = os.getenv("CURRENCY_CONVERTER_URL")
API_KEY = os.getenv("API_KEY")
