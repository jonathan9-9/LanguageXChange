from django.contrib import admin
from django.urls import path
from accounts.views import api_list_user, api_show_user

urlpatterns = [
    path('users/', api_list_user, name='api_list_user'),
    path('users/<int:id>/', api_show_user, name='api_show_user'),
]
