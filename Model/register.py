from sqlalchemy import Column, Integer,String,Date,BigInteger
from Database.dbconnection import Base


class register(Base):
    __tablename__ = "register"
    id = Column(Integer, primary_key = True, nullable=False, autoincrement=True)
    firstname = Column(String, nullable =False)
    lastname = Column(String,nullable = False)
    phone = Column(BigInteger, nullable =False)
    email = Column(String,nullable = False, unique= True)
    dob = Column(Date, nullable = False)
    gender = Column(String,nullable = False)
    pwd = Column(String,nullable = False)


    






    
   

    




