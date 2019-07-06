from core.resources.base import BaseResource
from core.controllers.session_details import SessionDetailsController
from core.resources.argument_parser import PARSER


class SessionDetails(BaseResource):

    def get(self):
        args = PARSER.parse_args()
        sid = args['sid']
        session_details = SessionDetailsController()
        return session_details.get_details(sid)
