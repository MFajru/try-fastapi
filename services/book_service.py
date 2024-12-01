from sqlmodel import Session

from models.book import Author
from repositories.book_repository import add_author


def create_author(author:Author, session:Session):
    return add_author(author, session)