from fastapi import status, Depends,HTTPException,APIRouter
from sqlalchemy .orm import Session
from Util import util
from Database.dbconnection import get_db
from Model import register

router = APIRouter()

@router.post("/register",status_code=status.HTTP_201_CREATED)
def createdb(Post:dict,db : Session = Depends(get_db)): 
    msg=db.query(register.register).filter(register.register.email== Post['email'])
    if  msg.first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email ID already exist")
    
    else:
        hashed_pwd= util. hash(Post['pwd'])
        Post['pwd'] = hashed_pwd
        new = register.register(**Post)
        db.add(new)
        db.commit()
        db.refresh(new)
        return {"id":new.id , "email":new.email}