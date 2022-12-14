from sqlalchemy .orm import Session
from fastapi import Depends,status,HTTPException,APIRouter
from Model import register
from Authentication import oauth2
from Database.dbconnection import get_db

router = APIRouter()


@router.get("/userprofile/")
def retrive_data(db : Session = Depends(get_db),get_user : int= Depends(oauth2.get_current_user)):
    retrive =db.query(register.register).filter(register.register.id == get_user.id).first()
    # print(retrive.name,id)
    return retrive



@router.put("/up_userprofile/",status_code=status.HTTP_200_OK)
def updatepost(Post:dict,db : Session = Depends(get_db),get_user : int= Depends(oauth2.get_current_user)):
    p=db.query(register.register).filter(register.register.id == get_user.id)
    data= p.first()
    if data == None:        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {get_user.id} does not exist")
    else:
        p.update(Post,synchronize_session=False)
        db.commit()
        return {"Msg":p.first()} 


@router.delete("/del_userprofile/",status_code=status.HTTP_204_NO_CONTENT)
def deletepost(db : Session = Depends(get_db),get_user : int= Depends(oauth2.get_current_user)):
    p=db.query(register.register).filter(register.register.id== get_user.id)
    if p.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {get_user.id} does not exist")

    p.delete(synchronize_session=False)
    db.commit()
