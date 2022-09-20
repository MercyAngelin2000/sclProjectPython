from sqlalchemy .orm import Session
from fastapi import Depends,status,HTTPException,APIRouter
from model import models
from auth import oauth2
from database.database import get_db
router = APIRouter()


@router.get("/userprofile/")
def retrive_data(db : Session = Depends(get_db),get_user : int= Depends(oauth2.get_current_user)):
    retrive=db.query(models.register).filter(models.register.id == get_user.id).first()
    # print(retrive.name,id)
    return retrive



@router.put("/up_userprofile/",status_code=status.HTTP_200_OK)
def updatepost(Post:dict,db : Session = Depends(get_db),get_user : int= Depends(oauth2.get_current_user)):
    p=db.query(models.register).filter(models.register.id == get_user.id)
    data= p.first()
    if data == None:        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {get_user.id} does not exist")
    else:
        p.update(Post,synchronize_session=False)
        db.commit()
        return {"Msg":p.first()} 


@router.delete("/del_userprofile/",status_code=status.HTTP_204_NO_CONTENT)
def deletepost(db : Session = Depends(get_db),get_user : int= Depends(oauth2.get_current_user)):
    p=db.query(models.register).filter(models.register.id== get_user.id)
    if p.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {get_user.id} does not exist")

    p.delete(synchronize_session=False)
    db.commit()
