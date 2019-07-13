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
        # return response
        return json.dumps({
            'user_id': str(uuid4()),
            'username': username,
            'email': username + '@urk.net',
            'user_address': 'address 15/20',
            'create_user_date': datetime.now().__str__()
        })
