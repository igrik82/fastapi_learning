from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Depends, status, HTTPException
from models import User
from schema import TokenData
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database import get_db


oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth")

SECRET_KEY = "asdjflkeqwriouhdsiuafhpaiushdfjkhlskdjfhqwblkjvasdpuiwerbnkj341"
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTS = 300


def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_MINUTS)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_access_token(token: str, credential_exception) -> TokenData:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        # user_id same as in auth.py
        id: int = payload.get("current_user")

        if id is None:
            raise credential_exception

        token_data = TokenData(id=id)

    except JWTError:
        raise credential_exception

    return token_data


def get_current_user(
    token: str = Depends(oauth2_schema), db: Session = Depends(get_db)
):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    verifys_token: TokenData = verify_access_token(token, credential_exception)
    user = db.query(User).filter(User.id == verifys_token.id).first()
    return user
