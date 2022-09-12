from sqlalchemy import create_engine  #used to connect with db
from sqlalchemy.ext.declarative import declarative_base  #to collect the obj that defined in new table
from sqlalchemy.orm import sessionmaker # used to interact with db

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/SclProject"   #username:password@hostname/dbname
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Sessionlocal = sessionmaker(autocommit=False, autoflush=False,bind=engine) 
Base = declarative_base()    #we will inherit from this class to create each of the database models or classes

# Dependency
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()