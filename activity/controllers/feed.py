from flask_restful import Resource
from ..feed_managers import manager

class FeedAPI(Resource):
    def get(self, user_id):
        feed = manager.get_feeds(user_id)['aggregated']
        activities = list(feed[:25])
        response = [{
            'date': agg.updated_at.isoformat(),
            'activities': [{
                'actor': a.actor_id,
                'verb': a.verb.id,
                'object': a.object_id,
                'date': a.time.isoformat()
            } for a in agg.activities]
        } for agg in activities]
        return response
