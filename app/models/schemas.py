from pydantic import BaseModel
from uuid import uuid4
from typing import List, Dict


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: str = str(uuid4())

    class Config:
        orm_mode = True


class NoteBase(BaseModel):
    user_id: str
    cluster_name: str
    title: str
    content: str


class NoteCreate(NoteBase):
    pass


class Note(NoteBase):
    id: int

    class Config:
        orm_mode = True
