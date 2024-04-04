import requests
ENDPOINT_POST = "http://0.0.0.0:3000/api/ner/ner_post"
ENDPOINT_GET = "http://localhost:3000/api/ner/ner_get"
ENDPOINT_SIGNUP = "http://0.0.0.0:3000/api/auth/signup"
ENDPOINT_SIGNIN = "http://0.0.0.0:3000/api/auth/signin"
ENDPOINT_DELETE_NER = "http://0.0.0.0:3000/api/ner/ner_delete"


def test_ner_post():
    response1 = requests.post(ENDPOINT_SIGNIN, json={"password": "testpassword", 
                                         "email": "testuser@gmail.com"})
    token = response1.json()["token"]
    response2 = requests.post(ENDPOINT_POST, 
                             json={"text": "Apple is a company"},
                              headers={"Authorization": token})
    assert response2.status_code == 200
    expected_entities = {"0": {'text': 'Apple', 'label': 'ORG', 'start_char': 0, 'end_char': 5}}
    assert response2.json()['entities'] == expected_entities

    response3 = requests.get(ENDPOINT_GET, json={"text_id": response2.json()['text_id']},
                            headers={"Authorization": token})
    assert response3.status_code == 200


def test_ner_delete():
    response1 = requests.post(ENDPOINT_SIGNIN, json={"password": "testpassword", 
                                         "email": "testuser@gmail.com"})
    token = response1.json()["token"]
    response2 = requests.post(ENDPOINT_POST, 
                             json={"text": "Apple is a company"},
                              headers={"Authorization": token})
    assert response2.status_code == 200
    print(response2.json()['text_id'])
    response3 = requests.delete(ENDPOINT_DELETE_NER, json={"text_id": response2.json()['text_id']},
                            headers={"Authorization": token})
    assert response3.status_code == 200


