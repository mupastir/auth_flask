import pytest
from core.app import app


@pytest.fixture
def client():
    test_client = app.test_client()
    return test_client

