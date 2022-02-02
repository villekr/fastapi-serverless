from fastapi.testclient import TestClient
from fastapi_serverless.app import app
from fastapi_serverless.models.api import Author
from pydantic import parse_obj_as
from typing import List

client = TestClient(app)


def test_get():
    response = client.get("/authors")
    assert response.status_code == 200
    assert type(response.json() is dict)
    authors: List[Author] = parse_obj_as(List[Author], response.json())
    author: Author = authors[0]
    assert author.id == 1


def test_post():
    author: Author = Author(id=99, first_name="Test", last_name="Author")
    body: dict = dict(author)
    response = client.post("/authors", json=body)
    assert response.status_code == 201
    assert type(response.json() is dict)
    response_author: Author = parse_obj_as(Author, response.json())
    assert response_author == author
