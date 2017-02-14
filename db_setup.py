from cassandra.cqlengine.management import sync_table, create_keyspace_simple
from cassandra.cqlengine import connection
from cassandra import ConsistencyLevel

from activity.activity_feed import ActivityFeed, AggregatedActivityFeed

# It would be nice to import the setup parameters from the settings instead of hard-coding them
# here.
# from activity import settings

connection.setup(
    hosts=['cassandra'],
    consistency=ConsistencyLevel.ONE,
    default_keyspace='stream_framework',
    protocol_version=3
)

create_keyspace_simple('stream_framework', 1)
sync_table(ActivityFeed.get_timeline_storage().model)
sync_table(AggregatedActivityFeed.get_timeline_storage().model)
