from sqlmodel import Session

from models.book import Author, Book
from repositories.book_repository import add_author, add_book, select_all_author_books, select_books


def create_author(author:Author, session:Session):
    return add_author(author, session)

def create_book(book:Book, session: Session):
    return add_book(book, session)

def read_book(session: Session):
    return select_books(session)

def read_all_author_books(session: Session):
    return select_all_author_books(session)