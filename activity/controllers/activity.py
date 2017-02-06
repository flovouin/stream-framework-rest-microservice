from stream_framework.activity import Activity
from flask_restful import Resource, reqparse
from ..feed_managers import manager
from ..verbs import FollowVerb

class ActivityAPI(Resource):
    def get(self, id):
        return {'id': id}

class ActivityListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('actor', type=str, required=True, location='json')
        # self.reqparse.add_argument('verb', type=str, required=True, location='json')
        self.reqparse.add_argument('object', type=str, required=True, location='json')
        self.reqparse.add_argument('target', type=str, required=True, location='json')
        super(ActivityListAPI, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        activity = Activity(args['actor'], FollowVerb, args['object'], args['target'])
        # time=datetime.utcnow()
        # extra_context=dict(item_id=self.item_id)
        manager.add_user_activity(activity.actor_id, activity)
        return {'message': 'Created'}, 201
