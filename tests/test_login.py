import pytest
import requests

import json
from uuid import uuid4
from tests.conftest import USER_INFO
from core.constants import USERS_URL


def test_login(client, requests_mock):
    requests_mock.get(USERS_URL, text=USER_INFO)
    assert client.post('/auth/login').status_code == 200


