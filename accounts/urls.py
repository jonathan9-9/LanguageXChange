from django.urls import path
from accounts.views import (
    api_list_user,
    api_show_user,
    api_friends_list,
    api_friend_request,
    # api_cancel_friend_request,
    # api_delete_friend,
    # api_block_user,

)

urlpatterns = [
    path('users/', api_list_user, name='api_list_user'),
    path('users/<int:id>/', api_show_user, name='api_show_user'),
    path('friends/', api_friends_list, name='api_friends_list'),
    path('friends/<int:id>/', api_friend_request, name='api_friend_request'),
    # path('cancel/<int:id>/', api_cancel_friend_request, name='api_cancel_friend_request'),
    # path('delete/<int:id>/', api_delete_friend, name='api_delete_friend'),
    # path('block/<int:id>/', api_block_user, name='api_block_user'),
]
