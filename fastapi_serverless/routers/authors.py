from fastapi import APIRouter, Depends, HTTPException
from typing import List
from fastapi_serverless.models.api import Author
from fastapi_serverless.database import Database, get_db

router = APIRouter()


@router.get("/authors", tags=["authors"], response_model=List[Author])
async def get(db: Database = Depends(get_db)):
    return list(db.authors.values())


@router.get("/authors/{author_id}", tags=["authors"], response_model=Author)
async def get(author_id: int, db: Database = Depends(get_db)):
    if author_id not in db.authors:
        raise HTTPException(
            status_code=404, detail=f"Author with {author_id} not found."
        )
    return db.authors[author_id]


@router.post("/authors", tags=["authors"], status_code=201, response_model=Author)
async def post(author: Author, db: Database = Depends(get_db)):
    if author.id in db.authors:
        raise HTTPException(
            status_code=409, detail=f"Author with {author.id} already exists."
        )
    db.authors[author.id] = author
    return author
