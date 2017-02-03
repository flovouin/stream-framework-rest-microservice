from stream_framework.feeds.cassandra import CassandraFeed

class ActivityFeed(CassandraFeed):
    key_format = 'feed:%(user_id)s'

class UserActivityFeed(ActivityFeed):
    key_format = 'feed:user:%(user_id)s'
