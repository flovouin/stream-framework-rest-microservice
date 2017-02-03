from stream_framework.verbs import register
from stream_framework.verbs.base import Verb


class FollowVerb(Verb):
    id = 5
    infinitive = 'follow'
    past_tense = 'followed'

register(FollowVerb)
