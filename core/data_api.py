import requests
import json
from uuid import uuid4
import datetime


class AccessToUsers:

    @staticmethod
    def get(username):
        response = requests.get(f'http://localhost:5000/user/{username}')
        # return response
        return json.dumps({
            "id": str(uuid4()),
            "username": username,
            "email": username + '@gmail.com',
            "user_address": "Paramonova 25/7",
            "create_user_date": datetime.datetime.now().__str__()
        })
