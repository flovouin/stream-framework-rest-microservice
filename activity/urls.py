from django.conf.urls import url

from activity.controllers import activity, follow, feed

urlpatterns = [
    url(r'^activities', activity.post_activity),
    url(r'^feeds/(?P<user_id>[a-zA-Z0-9_]+)$', feed.get_feed),
    url(r'^follow', follow.post_follow)
]
