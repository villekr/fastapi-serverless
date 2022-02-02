import os

from fastapi import FastAPI
from mangum import Mangum

from fastapi_serverless.routers import books, authors, genres

STAGE = os.getenv("STAGE")
ROOT_PATH = None if STAGE is None else f"/{STAGE}/"

app = FastAPI(
    title="FastAPI serverless",
    description="Simple REST API using FastAPI in serverless (Lambda) environment.",
    root_path=ROOT_PATH,
)

app.include_router(books.router)
app.include_router(authors.router)
app.include_router(genres.router)

handler = Mangum(app)

if __name__ == "__main__":
    # Main is only needed for running uvicorn server when debugging in IDE
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
