from django.contrib import admin
from django.urls import path
import chat.views


urlpatterns = [
    path('', chat.views.room_list, name='room_list'),
    path('<room_name>/', chat.views.room_view, name='room')
]
