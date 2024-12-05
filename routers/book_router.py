from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlmodel import Session

from cmd.database.db import get_session
from dto.book_request import BookRequest
from dto.book_response import BookResponse
from models.book import Author, Book
from dto.author_request import AuthorRequest
from services.book_service import create_author, create_book, read_book

router = APIRouter()

@router.post("/add-author", response_model=Author)
def post_author(req: AuthorRequest,  session:Session = Depends(get_session)):
    new_author = Author(**req.model_dump())         # same as: (name = req.name, id = req.id) etc
    create_author(new_author, session)
    return new_author

@router.post("/add-book", response_model=Book)
def post_book(req: BookRequest, session: Session = Depends(get_session)):
    new_book = Book(**req.model_dump())
    create_book(new_book, session)
    return new_book

@router.get("/books", response_model=list[Book])
def get_book(session: Session = Depends(get_session)):
    books = read_book(session)
    return books