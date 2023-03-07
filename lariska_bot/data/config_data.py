import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

IP = str(os.getenv('IP'))
PG_USER = str(os.getenv('PG_USER'))
PG_PASSWORD = str(os.getenv('PG_PASSWORD'))
DATABASE = str(os.getenv('DATABASE'))

POSTGRES_URI = f'postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{IP}/{DATABASE}'
