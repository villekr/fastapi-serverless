from typing import List
from datetime import datetime
from pydantic import BaseModel


class Model(BaseModel):
    id: int

    class Meta:
        primary_key_name = "PK"
        sort_key_name = "SK"


class Author(Model):
    first_name: str
    last_name: str


class Book(Model):
    name: str
    published: datetime
    author_id: int


class Genre(Model):
    name: str
    book_ids: List[int]
