import json
from uuid import uuid4
from http import HTTPStatus

from core.constants import USERS_URL

class TestLogin:

    def test_login_success(self, client, mocker):
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
        mocker.patch('core.utils.data_api.AccessToUsers.post', return_value=json.dumps(user_info))
        with client.post('/auth/login', data=json.dumps(data), content_type=mimetype) as response:
            assert response.status_code == HTTPStatus.OK
            assert response.json["status"] == "success"
            assert response.content_type == mimetype

    def test_login_failed(self, client, mocker):
        mimetype = 'application/json'
        data = {
            'username': "test",
            'password': "test"
        }
        user_info = {"info": "user doesn't exist"}
        mocker.patch('core.utils.data_api.AccessToUsers.post', return_value=json.dumps(user_info))
        with client.post('/auth/login', data=json.dumps(data), content_type=mimetype) as response:
            assert response.status_code == HTTPStatus.BAD_REQUEST
            assert response.json["status"] == "failure"
            assert response.content_type == mimetype

    def test_login_wrong_input(self, client, mocker):
        mimetype = 'application/json'
        data = {
            'user': "test"
        }
        user_info = {"info": "user doesn't exist"}
        mocker.patch('core.utils.data_api.AccessToUsers.post', return_value=json.dumps(user_info))
        with client.post('/auth/login', data=json.dumps(data), content_type=mimetype) as response:
            assert response.status_code == HTTPStatus.BAD_REQUEST
            assert response.json["status"] == "failure"
            assert response.content_type == mimetype