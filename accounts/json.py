from json import JSONEncoder
from django.db.models import QuerySet
from .models import User, Language, FriendsList, BlockedUser


class LanguageEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Language):
            return {
                'id': o.id,
                'name': o.name
            }
        return super().default(o)

class FriendsListEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, FriendsList):
            return {
                'id': o.id,
                'sender': o.sender,
                'recipient': o.recipient
            }
        return super().default(o)

class BlockedUserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, BlockedUser):
            return {
                'id': o.id,
                'blocked_by': o.blocked_by,
                'blocked_user': o.blocked_user
            }
        return super().default(o)
