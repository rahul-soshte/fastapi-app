from pydantic import BaseModel
from typing import Optional

class PostBase(BaseModel):
    author: str
    body: str

class PostCreate(BaseModel):
    author: str
    body: str

class Post(PostBase):
    id: str
