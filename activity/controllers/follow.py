from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..services import follow

@api_view(['POST'])
def post_follow(request):
    data = request.data
    follow.follow(data['follower'], data['following'])
    return Response(status=201)
