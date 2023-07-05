"""Pydantics schema"""
from datetime import datetime
from enum import IntEnum
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


# Votes input schema
class Choices(IntEnum):
    liked = 1
    disliked = 0


class Votes(BaseModel):
    vote: Choices
    post_id: int


class VotesOut(BaseModel):
    id: int

    class Config:
        orm_mode = True


class ResponsePydan(BasePydantic):
    id: int
    created_at: datetime
    owner_id: int
    owner: OutUser
    # make_vote: VotesOut


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
