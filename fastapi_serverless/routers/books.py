from fastapi import APIRouter, Depends, HTTPException
from typing import List
from fastapi_serverless.models.api import Book
from fastapi_serverless.database import Database, get_db

router = APIRouter()


@router.get("/books", tags=["books"], response_model=List[Book])
async def get(db: Database = Depends(get_db)):
    return list(db.books.values())


@router.get("/books/{book_id}", tags=["books"], response_model=Book)
async def get(book_id: int, db: Database = Depends(get_db)):
    if book_id not in db.books:
        raise HTTPException(status_code=404, detail=f"Book with {book_id} not found.")
    return db.books[book_id]


@router.post("/books", tags=["books"], status_code=201, response_model=Book)
async def post(book: Book, db: Database = Depends(get_db)):
    if book.id in db.books:
        raise HTTPException(
            status_code=409, detail=f"Book with {book.id} already exists."
        )
    db.books[book.id] = book
    return book
