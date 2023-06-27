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


class OutUser(BaseModel):
    login: str
    email: EmailStr

    class Config:
        orm_mode = True


class InUser(OutUser):
    password: str


class UserAuth(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
