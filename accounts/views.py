from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import FriendsList, BlockedUser
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def friends_list(request):
    users = User.objects.exclude(user=request.user)
    context = {
        'users': users
    }
    return render(request, "accounts/home.html", context)

@login_required
def send_friend_request(request, user_id):
    from_user = request.user
    to_user = User.objects.get(id=user_id)
    created = FriendsList.objects.get_or_create(
        from_user=from_user,
        to_user=to_user
    )
    if created:
        return HttpResponse('Friend request sent')
    else:
        return HttpResponse('Friend request was already sent')

@login_required
def accept_friend_request(request, request_id):
    friends_list = FriendsList.objects.get(id=request_id)
    if friends_list.to_user == request.user:
        friends_list.to_user.friends.add(friends_list.from_user)
        friends_list.from_user.friends.add(friends_list.to_user)
        friends_list.delete()
        return HttpResponse('Friend request accepted')
    else:
        return HttpResponse('Friend request denied')

@login_required
def cancel_friend_request(request, request_id):
    friends_list = get_object_or_404(FriendsList, id=request_id)
    if friends_list.to_user == request.user:
        friends_list.delete()
        return HttpResponse('Friend request canceled')
    else:
        return HttpResponse('Cannot cancel this friend request')

@login_required
def delete_friend(request, friend_id):
    friend = get_object_or_404(FriendsList, id=friend_id)

    if request.user == friend.from_user or request.user == friend.to_user:
        friend.delete()
        return HttpResponse('Friend deleted')
    else:
        return HttpResponse('Cannot delete this friend')

@login_required
def block_user(request, user_id):
    user_to_block = get_object_or_404(User, id=user_id)

    if BlockedUser.objects.filter(blocked_by=request.user, blocked_user=user_to_block).exists():
        return HttpResponse('User is already blocked')

    blocked_user, created = BlockedUser.objects.get_or_create(
        blocked_by=request.user,
        blocked_user=user_to_block
    )

    if created:
        return HttpResponse('User blocked')
    else:
        return HttpResponse('User is already blocked')
