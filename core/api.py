import datetime
import decimal
import json
import uuid

from flask import request, Response
from flask_restful import Api


class Api(Api):
    def __init__(self, *args, **kwargs):
        super(Api, self).__init__(*args, **kwargs)
        self.representation = {
            'application/json': output_json
        }


def output_json(data, code, headers=None):
    headers = headers or {}
    output_data = {
        "response_datetime": str(datetime.datetime.utcnow().isoformat()),
        "status": "failure" if code >= 400 else "success",
        "message" if isinstance(data, str) else "data": data
    }
    output_data = json.dumps(output_data)

    return Response(output_data, code, headers=headers, content_type="application/json")
