from sqlmodel import Session

from models.book import Author


def add_author(author: Author, session:Session) -> Author:
    session.add(author)
    session.commit()
    session.refresh(author)
    return author