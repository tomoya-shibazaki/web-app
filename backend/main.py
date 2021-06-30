from fastapi import FastAPI
from db import session
from models import Users
from schemas import User
from typing import List

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users", response_model=List[User])
def read_users():
    users = session.query(Users).all()
    return users