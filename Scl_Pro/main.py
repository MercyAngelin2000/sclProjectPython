from http.client import HTTPException
from fastapi import FastAPI, status, Depends,HTTPException
from sqlalchemy .orm import Session
from Scl_Pro import models,utils,oauth2
from Scl_Pro.database import engine,get_db
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine) # bind = A Connectable used to access the database Meta= collection of table objects

app = FastAPI()
origins = [
    # "http://localhost.tiangolo.com",
    # "https://localhost.tiangolo.com",
    # "http://localhost",
    "http://localhost:4200",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/login")
def login(data: OAuth2PasswordRequestForm = Depends(),db : Session = Depends(get_db)):
    print(data.username)
    mail=db.query(models.register).filter(models.register.email== data.username).first() 
    if not mail:
        return HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
    
    if not utils.verify(data.password,mail.pwd):
        return HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
    
    access_token = oauth2.create_access_token(data={"user_id":mail.id})
    return {"access_token":access_token,"token_type":"bearer"}


@app.post("/register",status_code=status.HTTP_201_CREATED)
def createdb(Post:dict,db : Session = Depends(get_db)): 
    print(Post)
    msg=db.query(models.register).filter(models.register.email== Post['email']).first()
    if  msg:
        return {"Msg":"Email Id Already Exist"}
    else:
        hashed_pwd= utils. hash(Post['pwd'])
        Post['pwd'] = hashed_pwd
        new = models.register(**Post)
        db.add(new)
        db.commit()
        db.refresh(new)
        return {"Data":new.id}
    

@app.get("/userprofile/")
def retrive_data(db : Session = Depends(get_db),get_user : int= Depends(oauth2.get_current_user)):
    retrive=db.query(models.register).filter(models.register.id == get_user.id).first()
    # print(retrive.name,id)
    return retrive



@app.put("/up_userprofile/")
def updatepost(Post:dict,db : Session = Depends(get_db),get_user : int= Depends(oauth2.get_current_user)):
    p=db.query(models.register).filter(models.register.id == get_user.id)
    data= p.first()
    if data == None:        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {get_user.id} does not exist")
    else:
        p.update(Post,synchronize_session=False)
        db.commit()
        return {"Msg":p.first()} 

@app.post("/sclprofile",status_code=status.HTTP_201_CREATED)
def insertdata(Post:dict,db:Session = Depends(get_db),get_user : int= Depends(oauth2.get_current_user)): 
    p=db.query(models.Scl_Profile).filter(models.Scl_Profile.owner_id==get_user.id)

    if not p.first():
        new = models.Scl_Profile(owner_id=get_user.id,**Post)
        db.add(new)
        db.commit()
        db.refresh(new)
        # return {"Data":new.id}
        return{"data":new}
    else:
        p.update(Post,synchronize_session=False)
        db.commit()
        return {"Msg":p.first()} 


@app.get("/sclprofile/")
def retrive_data(db : Session = Depends(get_db),get_user : int= Depends(oauth2.get_current_user)):
    retrive=db.query(models.Scl_Profile).filter(models.Scl_Profile.owner_id == get_user.id).first()
    print(retrive)
    return retrive

@app.delete("/del_userprofile/",status_code=status.HTTP_204_NO_CONTENT)
def deletepost(db : Session = Depends(get_db),get_user : int= Depends(oauth2.get_current_user)):
    p=db.query(models.register).filter(models.register.id== get_user.id)
    if p.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {get_user.id} does not exist")

    p.delete(synchronize_session=False)
    db.commit()
    
    # return Response(status_code=status.HTTP_204_NO_CONTENT)
