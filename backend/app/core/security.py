from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
import hashlib

SECRET_KEY = "n2ZQJ1f7RzvEwM3XyLqAq9yYz9Hn7s5fGkP0zZx1J8vU2a3b4c5d6e7f8g"

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed


def verify(plain_password:str, hashed_password: str) -> bool:
    return hash_password(plain_password) == hashed_password


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
