import sys
import os

from starlette.status import HTTP_404_NOT_FOUND
from database import get_db
from fastapi import Depends, FastAPI, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from schema import UserAuth
from models import User
from utils import verify_pass

# importing from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


router = APIRouter(tags=["authentication"])


@router.post(
    "/auth", status_code=status.HTTP_202_ACCEPTED  # , response_model=UserAuth
)
def auth(user_credetials: UserAuth, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_credetials.email).first()

    if user is None:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail="Invalid credentials"
        )

    password = verify_pass(user_credetials.password, user.password)
    if not password:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail="Invalid credentials"
        )
    return {"tocken": user}
