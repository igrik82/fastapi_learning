import sys
import os

from database import get_db
from fastapi import Depends, FastAPI, status, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from schema import SendToken
from models import User
from utils import verify_pass
from oauth2 import create_token

# importing from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


router = APIRouter(tags=["authentication"])


@router.post(
    "/auth", status_code=status.HTTP_202_ACCEPTED, response_model=SendToken
)
def auth(
    user_credetials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = (
        db.query(User).filter(User.email == user_credetials.username).first()
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials"
        )

    password = verify_pass(user_credetials.password, user.password)
    if not password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials"
        )

    access_token = create_token(data={"current_user": user.id})

    return {"token": access_token, "token_type": "Bearer"}
