from Schema import schema
from jose import jwt
from Configuration.config import setting
import pytest

def test_getmethod(client):
    res = client.get("/")
    print(res.json().get("Hai"))
    assert res.json().get("Hai") == "Hai da"

def test_login(client,test_user):
    res = client.post("/login",data={"username":test_user['email'],"password":test_user['password']})
    login_res = schema.Token(**res.json())
    payload = jwt.decode(login_res.access_token,setting.secret_key,setting.algorithm)
    id:str = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200

@pytest.mark.parametrize("email,password,status_code,detail",[
    ('wrongemail@gmail.com','mylu',403,'Invalid Credentials'),
    ('mercy@gmail.com','uioruiouio',403,'Invalid Credentials'),

])
def test_wrong_user(client,test_user,email,password,status_code,detail):
    res = client.post("/login",data={"username":email,"password":password})
    assert res.status_code == status_code
    assert res.json().get('detail')== detail

def test_get_all_posts(authorized_client):
    res = authorized_client.get("/userprofile/")
    print(res.json())
    assert res.status_code == 200

def test_update_posts(authorized_client):
    res = authorized_client.put("/up_userprofile/",json = {"firstname":"Mercy","lastname":"Angel","phone":"8778451528","email":"mercy@gmail.com","dob":"2000-08-04","gender":"female","pwd":"mylu"})
    print(res.json())
    assert res.status_code == 200
   
def test_delete_posts(authorized_client):
    res = authorized_client.delete("/del_userprofile/")
    assert res.status_code == 204
    