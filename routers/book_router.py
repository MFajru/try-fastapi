from fastapi import APIRouter, Depends
from sqlmodel import Session

from cmd.database.db import get_session
from models.book import Author
from dto.author_request import AuthorRequest
from repository.book_repository import add_author

router = APIRouter()

@router.get("/{id}")
def get_book(id: int):
    return {"data": {"name": "book"}}

@router.post("/add-author", response_model=Author)
def post_author(req: AuthorRequest,  session:Session = Depends(get_session)):
    new_author = Author(**req.model_dump())         # same as: (name = req.name, id = req.id) etc
    add_author(new_author, session)
    return new_author