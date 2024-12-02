from datetime import datetime
from sqlmodel import Field, SQLModel


class BookRequest(SQLModel, table = False):
    title: str
    published_date: datetime
    author_id: int

    class Config:
        extra = "forbid"