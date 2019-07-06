from flask_restful import reqparse


def create_parser():
    parser = reqparse.RequestParser()
    parser.add_argument('username')
    parser.add_argument('sid', type=str)
    return parser


PARSER = create_parser()
