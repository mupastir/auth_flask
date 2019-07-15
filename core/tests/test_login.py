import pytest


def test_login(client):
    assert client.post('/auth/login').status_code == 200
