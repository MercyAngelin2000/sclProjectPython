from fastapi.testclient import TestClient
from Database.database import get_db,Base
from Controller.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
import pytest
from Configuration.config import setting
from Authentication.oauth2 import create_access_token

SQLALCHEMY_DATABASE_URL = f"postgresql://{setting.database_username}:{setting.database_password}@{setting.database_hostname}:{setting.database_port}/{setting.database_name}_test"  #username:password@hostname/dbname

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionlocal = sessionmaker(autocommit=False, autoflush=False,bind=engine) 

@pytest.fixture
def session():
    # print(SQLALCHEMY_DATABASE_URL)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionlocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)

@pytest.fixture
def test_user(client):
    user_data = {"firstname":"Mercy","lastname":"Angelin","phone":"8765432876","email":"mercy@gmail.com","dob":"2000-08-04","gender":"female","pwd":"mylu"}
    res = client.post("/register",json=user_data)
    print(res.json())
    new_user = res.json()
    new_user['password'] = user_data['pwd']
    return new_user

@pytest.fixture
def token(test_user):
    return create_access_token({"user_id":test_user['id']})

@pytest.fixture
def authorized_client(client,token):
    client.headers = {
        **client.headers,
        "Authorization":f"bearer {token}"
       
    }
    return client

