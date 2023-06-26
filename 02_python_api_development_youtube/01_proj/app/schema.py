"""Pydantics schema"""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


class BasePydantic(BaseModel):
    title: str
    content: str
    published: Optional[bool] = False
    rating: Optional[int]

    class Config:
        orm_mode = True


class CreateUpdatePostPydan(BasePydantic):
    pass


class ResponsePydan(BasePydantic):
    id: int
    created_at: datetime


class PostUser(BaseModel):
    login: str
    email: EmailStr

    class Config:
        orm_mode = True


class User(PostUser):
    password: str
