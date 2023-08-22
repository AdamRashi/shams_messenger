import os
from dotenv import load_dotenv
import pathlib


dotenv_path = pathlib.Path(__file__).parents[3] / '.env.example'
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


DB_DRIVER = os.getenv('DB_DRIVER')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')


DATABASE_URL = f'postgresql+{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
