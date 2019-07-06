import requests


class AccessToUsers:

    @staticmethod
    def get(username):
        response = requests.get(f'http://localhost:5000/user/{username}')
        return response
