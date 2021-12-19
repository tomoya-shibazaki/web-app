"""main"""
from typing import List

from db import session
from fastapi import FastAPI
from models import Users
from schemas import User

app = FastAPI()


@app.get("/")
async def root():
    """root api endpoint."""
    return {"message": "Hello World"}


@app.get("/users", response_model=List[User])
def read_users():
    """users api endpoint."""
    users = session.query(Users).all()
    return users
