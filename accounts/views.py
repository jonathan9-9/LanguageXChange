from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import User, FriendsList
from accounts.common.json import ModelEncoder
from django.contrib.auth.models import User
from .models import User
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import RegistrationForm

import json


class UsersListEncoder(ModelEncoder):
    model = User
    properties = [
        "id",
        "first_name",
        "last_name",
        "username",
        "city",
        "state",
        "country",
    ]


class UserDetailEncoder(ModelEncoder):
    model = User
    properties = [
        "id",
        "first_name",
        "last_name",
        "username",
        "password",
        "city",
        "state",
        "country",
    ]

class FriendsListEncoder(ModelEncoder):
    model = FriendsList
    properties = [
        'id',
        'sender',
        'recipient',
    ]

# class BlockedUserEncoder(ModelEncoder):
#     model = BlockedUser
#     properties = [
#         'id',
#         'blocked_by',
#         'blocked_user',
#     ]



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})



@login_required
@require_http_methods(["GET", "DELETE", "PUT"])
def api_show_user(request, id):
    if request.method == "GET":
        try:
            user = User.objects.get(id=id)
            return JsonResponse(
                user,
                encoder=UsersListEncoder,
                safe=False
            )
        except User.DoesNotExist:
            response = JsonResponse({"message": "Account does not exist"})
            response.status_code = 404
            return response
    elif request.method == "DELETE":
        try:
            count, _= User.objects.filter(id=id).delete()
            return JsonResponse({"deleted": count > 0})
        except User.DoesNotExist:
            return JsonResponse({"message": "Account does not exist"})
    else:
        content = json.loads(request.body)
        User.objects.filter(id=id).update(**content)
        user = User.objects.get(id=id)
        return JsonResponse(
            user,
            encoder=UsersListEncoder,
            safe=False,
        )


@require_http_methods(["GET", "POST"])
def api_list_user(request):
    if request.method == "GET":
        users = User.objects.all()
        return JsonResponse(
            {"users": users},
            encoder=UserDetailEncoder,
            safe=False,
        )
    else:
        try:
            content = json.loads(request.body)
            user = User.objects.create(**content)
            return JsonResponse(
                user,
                encoder=UserDetailEncoder,
                safe=False,
            )
        except:
            response = JsonResponse(
                {"message": "Cannot create a user"}
            )
            response.status_code = 400
            return response

@login_required
@require_http_methods(["GET"])
def api_friends_list(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            try:
                sender_friends = FriendsList.objects.filter(sender=request.user)
                return JsonResponse(
                    {"friends": sender_friends},
                    encoder=FriendsListEncoder,
                )
            except FriendsList.DoesNotExist:
                return JsonResponse(
                    {"message": "No friends exist"},
                    status=404,
                )
        else:
            return JsonResponse(
                {"message": "User is not authenticated"},
                status=401,
            )

@login_required
@require_http_methods(["POST", "PUT", "DELETE"])
def api_friend_request(request, id=None):
    if request.method == "POST":
        data = json.loads(request.body)
        sender_id = data.get("sender")
        recipient_id = data.get("recipient")

        try:
            sender = User.objects.get(id=sender_id)
            recipient = User.objects.get(id=recipient_id)
        except User.DoesNotExist:
            return JsonResponse({"message": "User not found"}, status=404)

        friend_request = FriendsList.objects.create(
            sender=sender,
            recipient=recipient
        )

        return JsonResponse({"message": "Friend request sent"}, status=201)

    elif request.method == "PUT":
        try:
            friend = FriendsList.objects.get(id=id)
            friend.save()
            friend_data = {
                "id": friend.id,
                "sender": friend.sender.id,  # Convert sender to ID
                "recipient": friend.recipient.id,  # Convert recipient to ID
            }
            return JsonResponse(
                friend_data,
                safe=False,
                status=200
            )
        except FriendsList.DoesNotExist:
            return JsonResponse(
                {"message": "Could not accept or cancel friend request"},
                status=400,
            )

    elif request.method == "DELETE":
        count, _ = FriendsList.objects.filter(id=id).delete()
        if count > 0:
            return JsonResponse({'message': 'Friend deleted'})
        else:
            return JsonResponse({'message': 'Friend not found'}, status=404)

    elif request.method == "GET":
        try:
            friends = FriendsList.objects.all()
            return JsonResponse(
                {"friends": friends},
                encoder=FriendsListEncoder,
            )
        except FriendsList.DoesNotExist:
            return JsonResponse(
                {"message": "No friends exist"},
                status=404,
            )

# # @login_required
# @require_http_methods(["POST"])
# def api_block_user(request, id):

#   user_to_block = get_object_or_404(User, id=id)

#   if BlockedUser.objects.filter(blocked_by=request.user, blocked_user=user_to_block).exists():
#       return JsonResponse({'message': 'User is already blocked'}, status=400)

#   blocked_user, created = BlockedUser.objects.get_or_create(
#       blocked_by=request.user,
#       blocked_user=user_to_block
#   )

#   if created:
#       return JsonResponse(blocked_user, encoder=BlockedUserEncoder)
#   else:
#       return JsonResponse({'message': 'User is already blocked'}, status=400)
