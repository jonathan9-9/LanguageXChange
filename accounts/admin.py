from django.contrib import admin
from .models import Language, User, FriendsList
# Register your models here.

admin.site.register(Language)
admin.site.register(User)
admin.site.register(FriendsList)
