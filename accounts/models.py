from django.db import models

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=150)

class User(models.Model):
    first_name = models.CharField(max_length=150)
    last_name =  models.CharField(max_length=150)
    username =  models.CharField(max_length=150)
    password =  models.CharField(max_length=150)
    city =  models.CharField(max_length=150)
    state =  models.CharField(max_length=150)
    country =  models.CharField(max_length=150)

class FriendsList(models.Model):
    sender = models.ForeignKey(
        "User",
        related_name='sender',
        on_delete=models.CASCADE)

    recipient = models.ForeignKey(
        "User",
        related_name='recipient',
        on_delete=models.CASCADE)
