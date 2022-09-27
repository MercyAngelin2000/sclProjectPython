from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Controller import sclprofile
from Controller import login
from Controller import register
from Controller import userprofile


# models.Base.metadata.create_all(bind=engine) # bind = A Connectable used to access the database Meta= collection of table objects

app = FastAPI()

app.include_router(login.router)
app.include_router(register.router)
app.include_router(userprofile.router)
app.include_router(sclprofile.router)

origins = [
    "http://localhost:4200",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"Hai":"Hai da"}

