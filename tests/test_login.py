import json
from uuid import uuid4


from core.constants import USERS_URL


def test_login(client, requests_mock):
    mimetype = 'application/json'
    data = {
        'username': "test",
        'password': "test"
    }
    user_info = {
        "user_id": str(uuid4()),
        "username": "test",
        "email": "oleg@example.ru",
        "user_address": "Paramonova 27A/3",
        "create_user_date": "27.5.1"
    }
    requests_mock.post(USERS_URL, json=json.dumps(user_info))
    response = client.post('/auth/login', data=json.dumps(data))
    assert response.status_code == 200
    assert response.content_type == mimetype

