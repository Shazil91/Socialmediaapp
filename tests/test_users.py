import pytest
from jose import jwt
from app import schemas
from app.config import settings

    

# def test_root(client):
#     res = client.get("/")
#     print(res.json().get('Message'))
#     assert res.json().get('Message') == 'Hello World'
#     assert res.status_code == 200
    
def test_create_user(client):
    res = client.post("/users/", json={"email": "hello123@gmail.com", "password": "password123"})
    
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "hello123@gmail.com"
    assert res.status_code == 201
    
def test_login_user(client, test_user):
    res = client.post("/login", data={"username": test_user['email'], "password": test_user['password']})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200
    
@pytest.mark.parametrize("email, password, status_code", [
    ('wrongemail@gmail.com', 'password123', 403),
    ('hooria@gmail.com', 'wrongpassword', 403),
    ('wrongemail@gmail.com', 'wrongpassword', 403),
    (None, 'password123', 422),
    ('hooria@gmail.com', None, 422)
])
def test_incorrect_login(test_user, client, email, password, status_code):
    # Create the data dictionary only with non-None values
    data = {}
    if email is not None:
        data["username"] = email
    if password is not None:
        data["password"] = password

    # Send the request
    res = client.post("/login", data=data)

    # Assert the status code
    assert res.status_code == status_code