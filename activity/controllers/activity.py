from rest_framework.decorators import api_view
from rest_framework.response import Response
from stream_framework.activity import Activity
from ..feed_managers import manager
from ..verbs import FollowVerb

@api_view(['POST'])
def post_activity(request):
    data = request.data
    activity = Activity(data['actor'], FollowVerb, data['object'], data['target'])
    manager.add_user_activity(activity.actor_id, activity)
    return Response(status=201)
