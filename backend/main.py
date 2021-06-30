from fastapi import FastAPI
from db import session
from models import Users

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
def read_users():
    users = session.query(Users).all()
    return users