import requests

ENDPOINT_SIGNIN = "http://0.0.0.0:3000/api/auth/signin"
ENDPOINT_UPDATE = "http://0.0.0.0:3000/api/users/update_user"
ENDPOINT_GET = "http://0.0.0.0:3000/api/users/get_user"
def test_ner_update_firstname():
    response1 = requests.post(ENDPOINT_SIGNIN, json={"password": "testpassword", 
                                         "email": "testuser@gmail.com"})
    token = response1.json()["token"]
    response2 = requests.put(ENDPOINT_UPDATE, 
                             json={"firstname": "Tester101"},
                              headers={"Authorization": token})
    assert response2.status_code == 201

    response3 = requests.get(ENDPOINT_GET, json={},
                            headers={"Authorization": token})
    assert response3.json()['data']['firstname'] == "Tester101"
    assert response3.status_code == 200

def test_ner_update_lastname():
    response1 = requests.post(ENDPOINT_SIGNIN, json={"password": "testpassword", 
                                         "email": "testuser@gmail.com"})
    token = response1.json()["token"]
    response2 = requests.put(ENDPOINT_UPDATE, 
                             json={"lastname": "Tester101"},
                              headers={"Authorization": token})
    assert response2.status_code == 201

    response3 = requests.get(ENDPOINT_GET, json={},
                            headers={"Authorization": token})
    assert response3.json()['data']['lastname'] == "Tester101"
    assert response3.status_code == 200
