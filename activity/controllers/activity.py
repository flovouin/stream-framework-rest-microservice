import pytz
from datetime import datetime
from stream_framework.activity import Activity
from flask_restful import Resource
from ..feed_managers import manager
from ..verbs import FollowVerb

class ActivityAPI(Resource):
    def get(self, id):
        return {'id': id}

class ActivityListAPI(Resource):
    def post(self):
        activity = Activity(
            1234, # 'user_1234',
            FollowVerb,
            1234, #'act_1234',
            1234 #'influencer_1234'
            # time=datetime.utcnow()
            # extra_context=dict(item_id=self.item_id)
        )
        manager.add_user_activity(1234, activity)
        return {'message': 'Awesome!'}
