from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..feed_managers import manager

@api_view()
def get_feed(request):
    # This is the user ID specified in the JWT.
    user_id = request.user.username
    feed = manager.get_feeds(user_id)['aggregated']
    activities = list(feed[:25])
    # Simply gets the relevant fields from the activities, to avoid exposing implementation details.
    response = [{
        'date': agg.updated_at.isoformat(),
        'activities': [{
            'actor': a.actor_id,
            'verb': a.verb.infinitive,
            'object': a.object_id,
            'date': a.time.isoformat()
        } for a in agg.activities]
    } for agg in activities]
    return Response(response)
