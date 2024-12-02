from datetime import datetime, timezone
from sqlmodel import Field, Relationship, SQLModel


class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    published_date: datetime
    author_id: int = Field(foreign_key="author.id") 
    author: "Author" = Relationship(back_populates="books")
    created_at: datetime | None = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: datetime | None = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False, sa_column_kwargs={"onupdate": lambda: datetime.now(timezone.utc)})

class Author(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name:str
    books: list[Book] = Relationship(back_populates="author")
    created_at: datetime | None = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: datetime | None = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False, sa_column_kwargs={"onupdate": lambda: datetime.now(timezone.utc)})

    