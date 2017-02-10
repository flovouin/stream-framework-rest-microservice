from stream_framework.verbs import register
from stream_framework.verbs.base import Verb


class ActivityVerb(Verb):
    id = 5
    infinitive = 'verb'
    past_tense = 'verbed'

register(ActivityVerb)
