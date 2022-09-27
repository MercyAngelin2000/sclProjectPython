from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi import status, Depends,HTTPException,APIRouter
from sqlalchemy .orm import Session
from Authentication import oauth2
from Database.dbconnection import get_db
from Model import register
from Util import util

router = APIRouter()


@router.post("/login")
def login(data: OAuth2PasswordRequestForm = Depends(),db : Session = Depends(get_db)):
    print("haiii")
    mail=db.query(register.register).filter(register.register.email== data.username).first() 
    print(mail)
    if not mail:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
    
    if not util.verify(data.password,mail.pwd):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
    
    access_token = oauth2.create_access_token(data={"user_id":mail.id})
    return {"access_token":access_token,"token_type":"bearer"}
