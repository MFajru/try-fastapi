from datetime import datetime, timezone
from sqlalchemy import text
from sqlmodel import Field, SQLModel


class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    published_date: datetime
    created_at: datetime | None = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: datetime | None = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False, sa_column_kwargs={"onupdate": lambda: datetime.now(timezone.utc)})

class Author(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name:str
    created_at: datetime | None = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: datetime | None = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False, sa_column_kwargs={"onupdate": lambda: datetime.now(timezone.utc)})

    