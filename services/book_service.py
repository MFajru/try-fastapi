from sqlmodel import Session

from models.book import Author, Book
from repositories.book_repository import add_author, add_book


def create_author(author:Author, session:Session):
    return add_author(author, session)

def create_book(book:Book, session: Session):
    return add_book(book, session)