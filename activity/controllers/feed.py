from flask_restful import Resource
from ..feed_managers import manager

class FeedAPI(Resource):
    def get(self, user_id):
        feed = manager.get_feeds(user_id)['normal']
        activities = list(feed[:25])
        response = [{'actor': a.actor_id, 'verb': a.verb.id, 'object': a.object_id}
                    for a in activities]
        return response
