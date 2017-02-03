from stream_framework import settings
from stream_framework.feed_managers.base import Manager
from stream_framework.feed_managers.base import FanoutPriority
# from core.models import Follow
from activity.activity_feed import ActivityFeed, UserActivityFeed
from cassandra.cqlengine.management import sync_table, create_keyspace_simple

from activity.services import follow

class ActivityManager(Manager):
    feed_classes = dict(normal=ActivityFeed)
    user_feed_class = UserActivityFeed

    def get_user_follower_ids(self, user_id):
        followers = follow.get_followers(user_id)
        return {FanoutPriority.HIGH: followers}

manager = ActivityManager()

create_keyspace_simple(settings.STREAM_DEFAULT_KEYSPACE, 1)
sync_table(ActivityFeed.get_timeline_storage().model)
