from django.core.serializers import serialize
from django.utils.safestring import mark_safe
from .models import FriendsList, BlockedUser
import json

class ModelEncoder(json.JSONEncoder):
    def default(self, o):
        if hasattr(o, 'to_dict'):
            return o.to_dict()
        return super().default(o)

class FriendsListEncoder(ModelEncoder):
    def default(self, o):
        if isinstance(o, FriendsList):
            return {
                'sender': o.sender.id,
                'recipient': o.recipient.id,
            }
        return super().default(o)

class BlockedUserEncoder(ModelEncoder):
    def default(self, o):
        if isinstance(o, BlockedUser):
            return {
                'blocked_by': o.blocked_by.id,
                'blocked_user': o.blocked_user.id,
            }
        return super().default(o)

def custom_json_response(data, encoder_class):
    return mark_safe(json.dumps(data, cls=encoder_class))
