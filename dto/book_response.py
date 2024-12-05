from datetime import datetime
from sqlmodel import SQLModel


class BookResponse(SQLModel, table=False):
    id: int
    title: str
    published_date: datetime
    author_id: int
    created_at: datetime 
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }