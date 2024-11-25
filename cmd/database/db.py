import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlmodel import Session

load_dotenv()

db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
postgres_url = f'postgresql://{db_username}:{db_password}@{db_host}/{db_name}'

engine = create_engine(postgres_url)

def get_session():
    with Session(engine) as session:
        yield get_session()