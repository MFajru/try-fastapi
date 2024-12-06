from datetime import datetime
from sqlmodel import Field, SQLModel


class AuthorBookResponse(SQLModel, table=False):
    id: int | None = Field(default=None)
    name: str
    books: list["BookAuthorResponse"]


class BookAuthorResponse(SQLModel, table=False):
    id: int
    title: str
    published_date: datetime
   