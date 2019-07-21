import pytest
import json
from uuid import uuid4

def test_login(client):
    assert client.post('/auth/login').status_code == 200


user_id = json.dumps({
                "user_id": str(uuid4()),
                "username": "oleg",
                "email": "oleg@example.ru",
                "user_address": "Paramonova 27A/3",
                "create_user_date": "27.5.1"
        })
