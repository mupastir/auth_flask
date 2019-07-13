import requests
import json
from uuid import uuid4
from datetime import datetime


class AccessToUsers:

    @staticmethod
    def get(username, password):
        params = json.dumps({
            'username': username,
            'password': password
        })
        response = requests.get('http://localhost:5000/user/', params=params)
        return response
