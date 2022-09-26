from fastapi import status, Depends,HTTPException,APIRouter
from sqlalchemy .orm import Session
from Utils import utils
from Database.database import get_db
from Model import models

router = APIRouter()

@router.post("/register",status_code=status.HTTP_201_CREATED)
def createdb(Post:dict,db : Session = Depends(get_db)): 
    msg=db.query(models.register).filter(models.register.email== Post['email'])
    if  msg.first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email ID already exist")
    
    else:
        hashed_pwd= utils. hash(Post['pwd'])
        Post['pwd'] = hashed_pwd
        new = models.register(**Post)
        db.add(new)
        db.commit()
        db.refresh(new)
        return {"id":new.id , "email":new.email}