from fastapi import APIRouter, Depends
from sqlmodel import Session

from cmd.database.db import get_session
from dto.book_request import BookRequest
from dto.author_books_response import AuthorBookResponse
from models.book import Author, Book
from dto.author_request import AuthorRequest
from services.book_service import create_author, create_book, read_all_author_books, read_book

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

@router.get("/author-books")
def get_all_author_books(session: Session = Depends(get_session)):
    all_author_books = read_all_author_books(session)
    author_books_responses = []
    prev_id = 0
    for author, _ in all_author_books:
        
        if author.id == prev_id:
            continue

        author_books_response = AuthorBookResponse(
            id=author.id,
            name=author.name,
            books=author.books
        )
        author_books_responses.append(author_books_response)
        prev_id = author.id
    return author_books_responses