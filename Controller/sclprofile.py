from fastapi import status,Depends,APIRouter
from sqlalchemy .orm import Session
from Model import schoolProfile
from Authentication import oauth2
from Database.dbconnection import get_db

router = APIRouter()

@router.post("/sclprofile",status_code=status.HTTP_201_CREATED)
def insertdata(Post:dict,db:Session = Depends(get_db),get_user : int= Depends(oauth2.get_current_user)): 
    print(get_user)
    p=db.query(schoolProfile.Scl_Profile).filter(schoolProfile.Scl_Profile.owner_id==get_user.id)

    if not p.first():
        new = schoolProfile.Scl_Profile(owner_id=get_user.id,**Post)
        db.add(new)
        db.commit()
        db.refresh(new)
        # return {"Data":new.id}
        return{"data":new}
    else:
        p.update(Post,synchronize_session=False)
        db.commit()
        return {"Msg":p.first()} 


@router.get("/sclprofile/")
def retrive_data(db : Session = Depends(get_db),get_user : int= Depends(oauth2.get_current_user)):
    retrive=db.query(schoolProfile.Scl_Profile).filter(schoolProfile.Scl_Profile.owner_id == get_user.id).first()
    print(retrive)
    return retrive

