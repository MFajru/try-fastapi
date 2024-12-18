import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlmodel import Session

load_dotenv()

db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
# db_url = f'postgresql://{db_username}:{db_password}@{db_host}/{db_name}'
# for mysql
db_url = f'mysql+pymysql://{db_username}:{db_password}@{db_host}/{db_name}'

engine = create_engine(db_url, pool_size=2, max_overflow=5, pool_recycle=3600)

def get_session():
    with Session(engine) as session:
        yield session