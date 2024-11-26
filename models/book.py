from datetime import datetime, timezone
from sqlalchemy import text
from sqlmodel import Field, SQLModel


class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    published_date: datetime
    # created_at: datetime = Field(default_factory=datetime.now(timezone.utc), sa_column_kwargs={"server_default": text("CURRENT_TIMESTAMP")})
    # updated_at: datetime = Field(default_factory=datetime.now(timezone.utc), sa_column_kwargs={"server_default": text("CURRENT_TIMESTAMP")})

class Author(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name:str
    # created_at: datetime = Field(default_factory=datetime.now(timezone.utc), sa_column_kwargs={"server_default": text("CURRENT_TIMESTAMP")})
    # updated_at: datetime = Field(default_factory=datetime.now(timezone.utc), sa_column_kwargs={"server_default": text("CURRENT_TIMESTAMP")})

    