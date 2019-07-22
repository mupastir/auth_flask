import pytest
import json
from uuid import uuid4
from core.app import app


@pytest.fixture
def client():
    test_client = app.test_client()
    return test_client

USER_INFO = json.dumps({
                "user_id": str(uuid4()),
                "username": "oleg",
                "email": "oleg@example.ru",
                "user_address": "Paramonova 27A/3",
                "create_user_date": "27.5.1"
        })
