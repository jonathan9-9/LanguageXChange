from django.contrib import admin
from .models import Language, User, FriendsList
# Register your models here.

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(FriendsList)
class FriendsListAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Language)
# admin.site.register(User)
# admin.site.register(FriendsList)
