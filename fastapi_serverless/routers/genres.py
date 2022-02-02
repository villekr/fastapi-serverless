from fastapi import APIRouter, Depends, HTTPException
from typing import List
from fastapi_serverless.models.api import Genre
from fastapi_serverless.database import Database, get_db

router = APIRouter()


@router.get("/genres", tags=["genres"], response_model=List[Genre])
async def get(db: Database = Depends(get_db)):
    return list(db.genres.values())


@router.get("/genres/{id}", tags=["genres"], response_model=Genre)
async def get(id: int, db: Database = Depends(get_db)):
    if id not in db.genres:
        raise HTTPException(status_code=404, detail=f"Genre with {id=} not found.")
    return db.genres


@router.post("/genres", tags=["genres"], status_code=201, response_model=Genre)
async def post(genre: Genre, db: Database = Depends(get_db)):
    if genre.id in db.genres:
        raise HTTPException(
            status_code=409, detail=f"Author with {genre.id} already exists."
        )
    db.genres[genre.id] = genre
    return genre
