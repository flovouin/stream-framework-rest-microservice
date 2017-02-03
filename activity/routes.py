from flask_restful import Api

from activity.controllers import activity, follow, feed

def configure(app):
    api = Api(app)
    api.add_resource(activity.ActivityAPI, '/activities/<int:id>', endpoint='activity')
    api.add_resource(activity.ActivityListAPI, '/activities', endpoint='activities')
    api.add_resource(follow.FollowListAPI, '/follow/<int:id>', endpoint='follow')
    api.add_resource(feed.FeedAPI, '/feeds/<int:user_id>', endpoint='feed')
