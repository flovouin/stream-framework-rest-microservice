_followers = {}

def follow(follower_id, followee_id):
    if followee_id in _followers:
        _followers[followee_id].add(follower_id)
    else:
        _followers[followee_id] = set([follower_id])

def unfollow(follower_id, followee_id):
    if followee_id in _followers and follower_id in _followers[followee_id]:
        _followers[followee_id].remove(follower_id)

def get_followers(user_id):
    if user_id in _followers:
        return list(_followers[user_id])
    return []
