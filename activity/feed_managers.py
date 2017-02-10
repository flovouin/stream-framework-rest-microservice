from stream_framework import settings
from stream_framework.feed_managers.base import Manager
from stream_framework.feed_managers.base import FanoutPriority
from activity.activity_feed import ActivityFeed, AggregatedActivityFeed, UserActivityFeed

from activity.services import follow

class ActivityManager(Manager):
    feed_classes = dict(normal=ActivityFeed, aggregated=AggregatedActivityFeed)
    user_feed_class = UserActivityFeed

    def get_user_follower_ids(self, user_id):
        followers = follow.get_followers(user_id)
        return {FanoutPriority.HIGH: followers}

manager = ActivityManager()
