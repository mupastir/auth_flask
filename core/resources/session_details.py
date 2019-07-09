from flask import make_response
from core.resources.base import BaseResource
from core.controllers.session_details import SessionDetailsController
from core.resources.argument_parser import PARSER


class SessionDetails(BaseResource):

    def get(self):
        args = PARSER.parse_args()
        sid = str(args['sid'])
        session_details = SessionDetailsController().get_details(sid)
        response = make_response(session_details)
        response.headers.extend({'Session-ID': sid})
        return response
