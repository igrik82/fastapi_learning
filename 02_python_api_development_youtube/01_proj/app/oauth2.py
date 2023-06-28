from datetime import datetime, timedelta
from jose import JWTError, jwt


SECRET_KEY = "asdjflkeqwriouhdsiuafhpaiushdfjkhlskdjfhqwblkjvasdpuiwerbnkj341"
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTS = 30


def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=TOKEN_EXPIRE_MINUTS)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt
