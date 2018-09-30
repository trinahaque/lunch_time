from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import re
import random
from datetime import datetime, date
Email_Regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    # registrations takes the input from the views and creates a new user
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

    # getCoffee takes input from getCoffee function in views and 
    # generates random colleague for coffee
    def getCoffee(self, pid):
        # retrieve the user in session
        user = User.objects.get(id=pid)
        # print "userId", user.id
        
        # receive a list of all users excluding the user itself 
        userList = User.objects.exclude(id=pid)
        # print "userList", userList

        # retrieve all the friends met for coffee before
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
        
        error = []
        if len(newFriendsList) < 1:
            error.append("You have met with everyone for coffee. Please get lunch this time")
            return (False, error)
        else: 
            newCoffeeFriend = random.choice(newFriendsList)
            # print "coffeeFriendId", newCoffeeFriend.first_name
          
            user.coffee_friends.add(newCoffeeFriend)
           
            return (True, newCoffeeFriend.id)

    def getLunch(self, pid, min_friend_number, max_friend_number):
        min_friend_number = min_friend_number
        max_friend_number = max_friend_number
        user = User.objects.get(id=pid)
        userList = User.objects.exclude(id=pid)
        lunchFriends = []
        errors = []

        oldLunchFriends = user.lunch_friends.all()
        friends_to_exclude = [friend.id for friend in oldLunchFriends]
        # newFriendsList provides list of all the friends not met for lunch before
        newFriendsList = User.objects.exclude(id__in=friends_to_exclude).exclude(id=pid)
        # print "newFriendsList", newFriendsList

        # generates a number between 2 and 4 inclusive
        count_of_friends = random.randint(min_friend_number, max_friend_number) 

        # if the system is new and the current user is the only user in the list
        # ask user to wait
        if len(userList) < 1:
            errors.append("You are the only one in the system. Please wait for others to join.")
            print "1", errors[0]
            return (False, errors)
        
        # if application only has 3 or 2 users, lunch group will have all the users in the system
        elif len(userList) < 3:
            for each_friend in userList:
                lunchFriends.append(each_friend)
            self.addLunchFriend(user, lunchFriends)
            print "2", lunchFriends
            # for new_friend in lunchFriends:
            #     print "2", new_friend.first_name
        
        # userList is greater than 3 or higher
        else:
            # when the number of newFriendsList is less than 2, add all the newFriendsList to 
            # lunchFriends, find the rest from old friends
            if len(newFriendsList) < 2:
                # lunchFriends = newFriendsList
                for each_friend in newFriendsList:
                    lunchFriends.append(each_friend)
                number_of_friends_needed = count_of_friends - len(lunchFriends)
                # print "needed", number_of_friends_needed
                oldFriends = random.sample(oldLunchFriends, number_of_friends_needed)
                lunchFriends += oldFriends
                print "3", lunchFriends
                # print "3 lunch", lunchFriends
                # print "old", oldFriends
                self.addLunchFriend(user, newFriendsList)
                # for new_friend in lunchFriends:
                #     print "3", new_friend.first_name
            
            # if the new friends are between 2 and 4, assign all of them to lunchFriends
            elif len(newFriendsList) >= min_friend_number and len(newFriendsList) <= max_friend_number:
                for each_friend in newFriendsList:
                    lunchFriends.append(each_friend)
                print "4", lunchFriends
                self.addLunchFriend(user, newFriendsList)
                # for new_friend in lunchFriends:
                #     print "4", new_friend.first_name
           
            # if the new friends are over 4
            else:
                lunchFriends = random.sample(newFriendsList, count_of_friends)
                print "5", lunchFriends
                self.addLunchFriend(user, lunchFriends)
                # for new_friend in lunchFriends:
                #     print "5", new_friend.first_name
        return (True, lunchFriends)

    # this function takes the user in session and friends list (called newFriendsList in the 
    # parameter) who are getting lunch with user this time. The fuctions adds those friends
    # to the database that keeps track of friends met with users for lunch
    def addLunchFriend(self, user, newFriendsList):
        if len(newFriendsList) > 0:
            for newFriend in newFriendsList:
                user.lunch_friends.add(newFriend)
            return True
        return False

        
# schema for a new user
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    coffee_friends = models.ManyToManyField('self')
    lunch_friends = models.ManyToManyField('self')
    objects = UserManager()


