import requests
import json
from core.constants import USERS_URL


class AccessToUsers:

    @staticmethod
    def post(username, password):
        params = json.dumps({
            'username': username,
            'password': password
        })
        response = requests.post(USERS_URL, json=params)
        return response.text
