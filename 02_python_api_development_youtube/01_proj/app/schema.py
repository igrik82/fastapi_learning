"""Pydantics schema"""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


class OutUser(BaseModel):
    login: str
    email: EmailStr

    class Config:
        orm_mode = True


class InUser(OutUser):
    password: str


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
    user_id: int
    owner: OutUser


class UserAuth(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class SendToken(BaseModel):
    token: str
    token_type: str
    # There is not database query. Config no needed


class TokenData(BaseModel):
    id: Optional[int] = None
