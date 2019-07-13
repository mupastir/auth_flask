from flask import make_response, request
from core.resources.base import BaseResource
from core.controllers.session_details import SessionDetailsController
from marshmallow import ValidationError


class SessionDetails(BaseResource):

    def get(self):
        data = request.get_json()
        try:
            self.session_id_schema.load(data)
            sid = data['sid']
            session_details = SessionDetailsController().get_details(sid)
            response = make_response(session_details)
            response.headers.extend({'Session-ID': sid})
            return response
        except ValidationError:
            return 500
