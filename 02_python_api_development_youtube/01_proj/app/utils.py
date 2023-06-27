"""Banch of utils for project"""
from passlib.context import CryptContext


# Settings for hash library
pwd_context = CryptContext(schemes=["bcrypt"])


# Hashing password
def hash_pass(password: str):
    return pwd_context.hash(password)


# Verify password
def verify_pass(plain_pass: str, hashed_pass: str):
    return pwd_context.verify(plain_pass, hashed_pass)
