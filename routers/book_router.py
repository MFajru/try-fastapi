from fastapi import APIRouter, Depends
from sqlmodel import Session

from models.book import Author
from cmd.database.db import get_session
from dto.author_request import AuthorRequest

router = APIRouter()

@router.get("/{id}")
def get_book(id: int):
    return {"data": {"name": "book"}}

@router.post("/add-author", response_model=Author)
def post_author(req: AuthorRequest, session:Session = Depends(get_session)):
    new_author = Author(id=req.id, name=req.name)
    session.add(new_author)
    session.commit()
    session.refresh(new_author)
    return new_author