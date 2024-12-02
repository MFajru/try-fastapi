from sqlmodel import Session

from models.book import Author, Book


def add_author(author: Author, session:Session) -> Author:
    session.add(author)
    session.commit()
    session.refresh(author)
    return author

def add_book(book:Book, session: Session) -> Book:
    session.add(book)
    session.commit()
    session.refresh(book)
    return book