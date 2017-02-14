from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..services import follow

@api_view(['POST'])
def post_follow(request):
    data = request.data
    follow.follow(data['follower'], data['following'])
    # Here, `manager.follow_feed` could be used to add existing activities to the follower's feed.
    return Response(status=201)
