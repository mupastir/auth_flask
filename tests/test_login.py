import json
from uuid import uuid4
from http import HTTPStatus

TEST_LOGIN_DATA = {
    'username': "test",
    'password': "test"
}
TEST_WRONG_LOGIN_DATA = {
    'user': 'test'
}
TEST_USER_INFO = {
    "user_id": str(uuid4()),
    "username": "test",
    "email": "oleg@example.ru",
    "user_address": "Paramonova 27A/3",
    "create_user_date": "27.5.1"
}
TEST_WRONG_USER_INFO = {
    "info": "user doesn't exist"
}
MIMETYPE = 'application/json'


class TestLogin:

    def test_login_success(self, client, mocker):
        mocker.patch('core.utils.data_api.AccessToUsers.post', return_value=json.dumps(TEST_USER_INFO))
        with client.post('/auth/login', data=json.dumps(TEST_LOGIN_DATA), content_type=MIMETYPE) as response:
            assert response.status_code == HTTPStatus.OK
            assert response.json["status"] == "success"
            assert response.content_type == MIMETYPE
            assert "response_datetime" in response.json.keys()
            assert "data" in response.json.keys()

    def test_user_doesnt_exist(self, client, mocker):
        mocker.patch('core.utils.data_api.AccessToUsers.post', return_value=json.dumps(TEST_WRONG_USER_INFO))
        with client.post('/auth/login', data=json.dumps(TEST_LOGIN_DATA), content_type=MIMETYPE) as response:
            assert response.status_code == HTTPStatus.BAD_REQUEST
            assert response.json["status"] == "failure"
            assert response.content_type == MIMETYPE
            assert "response_datetime" in response.json.keys()
            assert "message" in response.json.keys()

    def test_wrong_input_login_data(self, client, mocker):
        mocker.patch('core.utils.data_api.AccessToUsers.post', return_value=json.dumps(TEST_WRONG_USER_INFO))
        with client.post('/auth/login', data=json.dumps(TEST_WRONG_LOGIN_DATA), content_type=MIMETYPE) as response:
            assert response.status_code == HTTPStatus.BAD_REQUEST
            assert response.json["status"] == "failure"
            assert response.content_type == MIMETYPE
            assert "response_datetime" in response.json.keys()
            assert "message" in response.json.keys()
