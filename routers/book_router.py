from fastapi import APIRouter


router = APIRouter()

@router.get("/{id}")
def getBook(id: int):
    return {"data": {"name": "book"}}