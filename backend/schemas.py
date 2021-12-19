"""schemas"""
from pydantic import BaseModel


class User(BaseModel):
    """user schema."""
    id: int
    name: str
    email: str

    class Config:
        """config."""
        orm_mode = True
