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
        # print "userId", user.id
        
        # receive a list of all users excluding the user itself 
        userList = User.objects.exclude(id=pid)
        # print "userList", userList

        # retrieve all the friends met for coffee before
        # this is not working
        oldCoffeeFriends = user.coffee_friends.all()
        # print "user before", user.id
        # print "coffee friend", user.coffee_friends
        # print "all coffee", oldCoffeeFriends
        # for each in oldCoffeeFriends:
        #     print "old", each.first_name

        # remove old coffee friends from the friends list to 
        # find a list of new friends
        newFriendsList = []

        for nonFriend in userList:
            valid = True
            for friend in oldCoffeeFriends:
                if (nonFriend.id == friend.id):
                    valid = False
                    break
            if valid:
                newFriendsList.append(nonFriend)
        # print "new friends", newFriendsList
        # for friend in newFriendsList:
        #     print "newFriendList", friend.first_name

        error = []
        if len(newFriendsList) < 1:
            error.append("You have met with everyone for coffee. Please get lunch this time")
            return (False, error)
        else: 
            newCoffeeFriend = random.choice(newFriendsList)
            print "coffeeFriendId", newCoffeeFriend.first_name
            # before = user.coffee_friends.all()
            # for friend in before:
            #     print "before", friend.first_name
            user.coffee_friends.add(newCoffeeFriend)
            # print "user after", user.id
            after = user.coffee_friends.all()
            # print "afterr", after
            # for newFriend in after:
            #     print "after", newFriend.first_name
            # print "length", len(after)
            # if the user has had coffee with everyone
            return (True, newCoffeeFriend.id)


# schema for a new user
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    coffee_friends = models.ManyToManyField('self')
    lunch_friends = models.ManyToManyField('self')
    objects = UserManager()


