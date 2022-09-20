from schema import schema
from jose import jwt
from config.config import setting

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

def test_wrong_user(client,test_user):
    res = client.post("/login",data={"username":test_user['email'],"password":"uiuieuwr"})
    print(res.json())
    print(res.status_code)
    assert res.status_code == 403
    assert res.json().get('detail' )== "Invalid Credentials"