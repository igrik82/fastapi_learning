import sys
import os
from database import get_db
from schema import InUser, OutUser
from utils import hash_pass
import models
from fastapi import Depends, FastAPI, status, HTTPException, APIRouter
from sqlalchemy.orm import Session

# importing from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

router = APIRouter()


@router.post(
    "/users", response_model=OutUser, status_code=status.HTTP_201_CREATED
)
def create_user(user_data: InUser, db: Session = Depends(get_db)):
    hash_passwd = hash_pass(user_data.password)
    user_data.password = hash_passwd
    new_user = models.User(**user_data.dict())

    db.add(new_user)
    db.commit()
    # return back post
    db.refresh(new_user)

    return new_user


@router.get("/users/{id}", response_model=OutUser)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    return user
