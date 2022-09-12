from datetime import datetime,timedelta
from jose import JWTError,jwt
from Scl_Pro import models
from fastapi import Depends, status,HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy .orm import Session
from Scl_Pro.database import get_db

oauth2_schema =OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY,ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str, credential_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        id:str = payload.get("user_id")

        if id is None:
            raise credential_exception
        # token_data = schema.TokenData(id=id)
        token_data = id
    except JWTError:
        raise credential_exception
    return token_data

def get_current_user(token: str=Depends(oauth2_schema),db : Session = Depends(get_db)):
    credential_exception =HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials",headers={"www-Authenticate":"Bearer"})
    token=verify_access_token(token,credential_exception)
    cur_user = db.query(models.register).filter(models.register.id == token).first()
    return cur_user

