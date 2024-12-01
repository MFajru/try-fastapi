from fastapi import Depends
from sqlmodel import Session

from models.book import Author
from cmd.database.db import get_session


def add_author(author: Author, session:Session) -> Author:
    session.add(author)
    session.commit()
    session.refresh(author)
    return author