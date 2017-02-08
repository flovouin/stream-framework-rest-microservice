from django.conf.urls import url

from activity.controllers import activity, follow, feed

urlpatterns = [
    url(r'^activities', activity.post_activity),
    url(r'^feeds/aggregated$', feed.get_feed),
    url(r'^follow', follow.post_follow)
]
