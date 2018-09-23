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

        valid = True
        if len(first_name) < 1 or len(last_name) < 1:
            errors.append("A field can not be empty")
            valid = False
        else:
            # names
            if len(first_name) < 2 or len(last_name) < 2:
                errors.append("Name field needs at least two characters")
                valid = False
            elif first_name.isalpha() == False or last_name.isalpha() == False:
                errors.append("Name field needs to be all letters")
                valid = False
            
        if valid:
            distinct_list = User.objects.filter(first_name = first_name, last_name = last_name)
            if not distinct_list:
                user = User.objects.create(first_name=first_name, last_name=last_name)
                return (True, user)
            else:
                # valid_messages.append("Email already exists")
                errors.append("User already exist")

        return (False, errors)


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
