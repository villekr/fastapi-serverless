from dataclasses import dataclass
from pydantic import BaseModel
from typing import Dict
from fastapi_serverless.models.api import Book, Author, Genre
from datetime import datetime


# Instead of real db we'll use a simple class to store our data in this example

class Database(BaseModel):
    books: Dict[int, Book]
    authors: Dict[int, Author]
    genres: Dict[int, Genre]


# Add some data to "database"
authors = {1: Author(id=1, first_name="Yuval", last_name="Harari")}
books = {
    1: Book(
        id=1,
        name="Sapiens",
        published=datetime(year=2017, month=5, day=15),
        author_id=authors[1].id,
    )
}
genres = {1: Genre(id=1, name="Science", book_ids=[books[1].id])}

database = Database(books=books, authors=authors, genres=genres)


def get_db():
    return database
