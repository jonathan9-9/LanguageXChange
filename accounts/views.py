from django.shortcuts import render
from accounts.common.json import ModelEncoder

# from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from .models import User
import json
from django.http import JsonResponse


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


@require_http_methods(["GET", "DELETE", "PUT"])
def api_show_user(request, id):
    if request.method == "GET":
        try:
            user = User.objects.get(id=id)
            return JsonResponse(user, encoder=UsersListEncoder, safe=False)
        except User.DoesNotExist:
            response = JsonResponse({"message": "Account does not exist"})
            response.status_code = 404
            return response
    elif request.method == "DELETE":
        try:
            count, _ = User.objects.filter(id=id).delete()
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
            response = JsonResponse({"message": "Cannot create a user"})
            response.status_code = 400
            return response
