from stream_framework.feed_managers.base import Manager
from stream_framework.feed_managers.base import FanoutPriority
# from core.models import Follow
from activity.activity_feed import ActivityFeed, UserActivityFeed
from cassandra.cqlengine.management import sync_table, create_keyspace_simple

class ActivityManager(Manager):
    feed_classes = dict(normal=ActivityFeed)
    user_feed_class = UserActivityFeed

        # self.add_user_activity(pin.user_id, activity)
        # self.remove_user_activity(pin.user_id, activity)

    def get_user_follower_ids(self, user_id):
        return {FanoutPriority.HIGH:[1234]}

manager = ActivityManager()

# TODO(flo): Find the keyspace elsewhere.
create_keyspace_simple(ActivityFeed.get_timeline_storage().model._get_keyspace(), 1)
sync_table(ActivityFeed.get_timeline_storage().model)
