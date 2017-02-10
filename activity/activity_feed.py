from stream_framework.aggregators.base import RecentRankMixin, BaseAggregator
from stream_framework.feeds.cassandra import CassandraFeed
from stream_framework.feeds.aggregated_feed.cassandra import CassandraAggregatedFeed

class ActivityFeedAggregator(RecentRankMixin, BaseAggregator):
    def get_group(self, activity):
        verb = activity.verb.id
        date = activity.time.strftime('%Y-%m-%d-%H')
        group = '%0.3d-%s' % (verb, date)
        return group

class ActivityFeed(CassandraFeed):
    key_format = 'feed:%(user_id)s'

class AggregatedActivityFeed(CassandraAggregatedFeed):
    aggregator_class = ActivityFeedAggregator
    key_format = 'feed:aggregated:%(user_id)s'

class UserActivityFeed(ActivityFeed):
    key_format = 'feed:user:%(user_id)s'
