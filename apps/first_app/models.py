from __future__ import unicode_literals
from django.db import models
import re, bcrypt
from datetime import datetime, date
Email_Regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def registration(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        errors = []

        if len(first_name) < 1 or len(last_name) < 1:
            errors.append("A field can not be empty")
        else:
            distinct_list = User.objects.filter(first_name = first_name, last_name = last_name)
            if not distinct_list:
                user = User.objects.create(first_name=first_name, last_name=last_name)
            else:
                user = distinct_list[0]
            return (True, user)
        return (False, errors)

    def getCoffee(self, pid):
        userList = User.objects.exclude(id=pid)
        for user in userList:
            print user.id
        return (True, userList)

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

