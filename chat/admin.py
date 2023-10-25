from django.contrib import admin
from chat.models import Room, Message

# Register your models here.

@admin.register(Room)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(Message)
class LanguageAdmin(admin.ModelAdmin):
    pass
