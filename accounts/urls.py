from django.urls import path
from .views import (
    friends_list,
    send_friend_request,
    accept_friend_request,
    cancel_friend_request,
    delete_friend,
    block_user,

)

urlpatterns = [
    path('friends_list/', friends_list, name='friends_list'),
    path('send_friend_request/<int:user_id>/', send_friend_request, name='send_friend_request'),
    path('accept_friend_request/<int:friend_request_id>/', accept_friend_request, name='accept_friend_request'),
    path('cancel_friend_request/<int:cancel_request_id>/', cancel_friend_request, name='cancel_friend_request'),
    path('delete_friend/<int:delete_friend_id>/', delete_friend, name='delete_friend'),
    path('block_user/<int:block_user_id>/', block_user, name='block_user'),
]
