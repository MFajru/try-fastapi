from sqlmodel import Session, select

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

def select_books(session: Session) -> list[Book]:
    books = session.exec(select(Book)).all()
    return books

def select_all_author_books(session: Session):
    # author_books = session.exec(select(Author.id ,Author.name, Book.id, Book.title, Book.published_date).join(Book)).all()
    author_books = session.exec(select(Author, Book).join(Book)).all()
    return author_books