from stream_framework import settings
from stream_framework.feed_managers.base import Manager
from stream_framework.feed_managers.base import FanoutPriority
from activity.activity_feed import ActivityFeed, AggregatedActivityFeed, UserActivityFeed

from activity.services import follow

class ActivityManager(Manager):
    feed_classes = dict(normal=ActivityFeed, aggregated=AggregatedActivityFeed)
    user_feed_class = UserActivityFeed

    def get_user_follower_ids(self, user_id):
        # Here we use the mocked follow service to get the list of followers. In the official
        # example, Django is used to persist the graph to the disk. In a microservice architecture,
        # calls to another service and caching of these calls would probably be involved.
        followers = follow.get_followers(user_id)
        return {FanoutPriority.HIGH: followers}

manager = ActivityManager()
