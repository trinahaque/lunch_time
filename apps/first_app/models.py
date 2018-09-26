from __future__ import unicode_literals
from django.db import models
import re
import random
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
        # retrieve the user in session
        user = User.objects.get(id=pid)
        
        # query excludes the user itself 
        userList = User.objects.exclude(id=pid)
        # print "friendlist", friendList
        
        # retrieve all the friends met before
        oldCoffeeFriends = user.coffee_friends.all()
        print "old", oldCoffeeFriends
        
        error = []
        if len(userList) < 1:
            error.append("Please wait for other to join")
            return (False, error)
        else: 
            nonFriends = []
            for user in userList:
                print user.id
                for friend in oldCoffeeFriends.all():
                    # print "friend", friend
                    if friend.id == user.id:
                        break
                nonFriends.append(user.id)
        
        myCoffeeFriendId = random.choice(nonFriends)
        # print "coffeefriend", myCoffeeFriendId

        # add the new colleague to the coffee friends
        myCoffeeFriend = User.objects.get(id=myCoffeeFriendId)
        user.coffee_friends.add(myCoffeeFriend)

        # still getting the same user twice
        return (True, myCoffeeFriendId)

class CoffeeFriendManager(models.Manager):
    def getCof(self):
        pass

# schema for a new user
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    # coffee_friends = models.ForeignKey('self', default=None)
    coffee_friends = models.ManyToManyField('self')
    lunch_friends = models.ManyToManyField('self')
    objects = UserManager()


