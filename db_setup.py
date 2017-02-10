from cassandra.cqlengine.management import sync_table, create_keyspace_simple
from cassandra.cqlengine import connection
from cassandra import ConsistencyLevel

# from activity import settings
from activity.activity_feed import ActivityFeed, AggregatedActivityFeed

connection.setup(
    hosts=['cassandra'],
    consistency=ConsistencyLevel.ONE,
    default_keyspace='stream_framework',
    protocol_version=3
)

create_keyspace_simple('stream_framework', 1)
sync_table(ActivityFeed.get_timeline_storage().model)
sync_table(AggregatedActivityFeed.get_timeline_storage().model)
