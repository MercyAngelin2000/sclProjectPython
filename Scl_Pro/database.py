from sqlalchemy import create_engine  #used to connect with db
from sqlalchemy.ext.declarative import declarative_base  #to collect the obj that defined in new table
from sqlalchemy.orm import sessionmaker # used to interact with db
from Scl_Pro.config import setting

SQLALCHEMY_DATABASE_URL = f"postgresql://{setting.database_username}:{setting.database_password}@{setting.database_hostname}:{setting.database_port}/{setting.database_name}"   #username:password@hostname/dbname
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