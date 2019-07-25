import json
from uuid import uuid4
from http import HTTPStatus


TEST_SID = {
            'sid': str(uuid4())
        }
TEST_WRONG_SID = {
    'session_id': str(uuid4())
}
TEST_DATA_FROM_DB = {
    "user_info":
        {
            "create_user_date": "2019-07-23 10:11:53.816786",
            "user_address": "test",
            "email": "test@test.com",
            "username": "test",
            "user_id": "bd37100e-2ff1-498a-9257-00b806b52080"
        },
    "session_create_date": "2019-07-25T07:57:23.275844"
}
MIMETYPE = 'application/json'


class TestLogin:

    def test_sid_success(self, client, mocker):
        mocker.patch('core.controllers.controllers.SessionDetailsController.get_from_db',
                     return_value=json.dumps(TEST_DATA_FROM_DB))
        with client.get('/auth/sid', data=json.dumps(TEST_SID), content_type=MIMETYPE) as response:
            assert response.status_code == HTTPStatus.OK
            assert response.json["status"] == "success"
            assert response.content_type == MIMETYPE
            assert "response_datetime" in response.json.keys()
            assert "data" in response.json.keys()

    def test_session_doesnt_exist(self, client, mocker):
        mocker.patch('core.controllers.controllers.SessionDetailsController.get_from_db',
                     return_value=json.dumps({}))
        with client.get('/auth/sid', data=json.dumps(TEST_SID), content_type=MIMETYPE) as response:
            assert response.status_code == HTTPStatus.BAD_REQUEST
            assert response.json["status"] == "failure"
            assert response.content_type == MIMETYPE
            assert "response_datetime" in response.json.keys()
            assert "message" in response.json.keys()

    def test_wrong_input_login_data(self, client, mocker):
        with client.get('/auth/sid', data=json.dumps(TEST_SID), content_type=MIMETYPE) as response:
            assert response.status_code == HTTPStatus.BAD_REQUEST
            assert response.json["status"] == "failure"
            assert response.content_type == MIMETYPE
            assert "response_datetime" in response.json.keys()
            assert "message" in response.json.keys()
