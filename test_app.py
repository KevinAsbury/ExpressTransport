import os
import json
import pytest

import app

SECRET = 'KeepItSecretKeepItSafe'
TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5qTTJSVE5CUmtZd1FqRTRNRVV6UkRkRE5qTXhPRE5FTVRKRk1UWkJNREpFTlVRMlJUazNNUSJ9.eyJpc3MiOiJodHRwczovL2thLWRldi5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTUxODI3NzUzNDI4ODIyMTE1MDEiLCJhdWQiOlsibXlleHByZXNzd2F5IiwiaHR0cHM6Ly9rYS1kZXYuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU4NTA2MjU5NSwiZXhwIjoxNTg1MDY5Nzk1LCJhenAiOiJaS0wzRDNSall1azFlQndiR2k3WTNYUkZkc2xzRXdJdiIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6ZGVsaXZlcmllcyIsImRlbGV0ZTpkcml2ZXJzIiwiZ2V0OmRlbGl2ZXJpZXMiLCJnZXQ6ZHJpdmVycyIsInBhdGNoOmRlbGl2ZXJpZXMiLCJwYXRjaDpkcml2ZXJzIiwicG9zdDpkZWxpdmVyaWVzIiwicG9zdDpkcml2ZXJzIl19.DHqYjXesmqp6o-f6XuYi6Aoocga9AJcADwO84iN8sEmGx8wWDnyvvY-29JJF-a5p4xV8_kqzgtMpF8lMmUyP7XpjnskYG2Pzvxa2mtaqzGjRq8ZP_EkL40mcH_3twf0dE4-SBqSQJVny9kfU9i03OubZ4xWrUbL7SXgAs4IOWEQjaraZ8lX62iuw6dKDn6JOcR4bCcXz1gwnefn8rErUEn6HxeOAZn4eIV49u82_-Od761gECG5kAPVk6Rk2mv1Li01wzOk70coIf52zgKmPOLe7wjG4RXH3ku8zszfdXdsaPpi0ea90paeTLiv2bcM2cYgIzz9G6wAMTVd-J8TvZA'
EMAIL = 'Frodo@mordor.com'
PASSWORD = 'TheOneToRuleThemAll'

@pytest.fixture
def client():
    os.environ['JWT_SECRET'] = SECRET
    app.app.config['TESTING'] = True
    client = app.app.test_client()
    yield client


def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == 'Hello World!'

# def test_health(client):
#     response = client.get('/deliveries')
#     assert response.status_code == 200
#     assert response.json == 'To be implemented'

# def test_health(client):
#     response = client.get('/drivers')
#     assert response.status_code == 200
#     assert response.json == 'To be implemented'

# def test_auth(client):
#     body = {'email': EMAIL,
#             'password': PASSWORD}
#     response = client.post('/auth', 
#                            data=json.dumps(body),
#                            content_type='application/json')

#     assert response.status_code == 200
#     token = response.json['token']
#     assert token is not None
