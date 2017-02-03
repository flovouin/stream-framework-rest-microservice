from flask_restful import Resource, reqparse

from ..services import follow

class FollowListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('follower', type=int, required=True, location='json')
        self.reqparse.add_argument('following', type=int, required=True, location='json')

    def post(self):
        args = self.reqparse.parse_args()
        follow.follow(args['follower'], args['following'])
        return {"message": "Created"}, 201
