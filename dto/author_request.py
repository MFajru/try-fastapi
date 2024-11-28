from sqlmodel import SQLModel


class AuthorRequest(SQLModel, table=False):
    name: str

    class Config:
        extra = "forbid"    # forbid extra field, reject data if there is extra field in json request)