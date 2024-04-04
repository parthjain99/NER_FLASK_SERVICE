import requests

ENDPOINT_SIGNIN = "http://0.0.0.0:3000/api/auth/signin"
ENDPOINT_DELETE  = "http://0.0.0.0:3000/api/users/delete_user"
ENDPOINT_SIGNUP = "http://0.0.0.0:3000/api/auth/signin"
def admin_delete_user(email):
    response = requests.post(ENDPOINT_SIGNIN, json={"email": "admin@gmail.com","password": "test101"})
    token = response.json()['token']
    response = requests.post(ENDPOINT_DELETE, json={"email": email},
                            headers={"Authorization": token})
    
def test_signup():
    response1 = requests.post(ENDPOINT_SIGNUP, json={"password": "testpassword", 
                                         "email": "testuser101@gmail.com", 
                                         "firstname": "testuser",
                                        "lastname": "testuser"})
    assert response1.status_code == 200
    assert response1.json()["status"] == "success"
    assert "token" in response1.json()

    response2 = requests.post(ENDPOINT_SIGNIN, json={"password": "testpassword", 
                                         "email": "testuser101@gmail.com"})
    assert response2.status_code == 200
    assert response2.json()["status"] == "success"
    assert "token" in response2.json()

    admin_delete_user("testuser101@gmail.com")