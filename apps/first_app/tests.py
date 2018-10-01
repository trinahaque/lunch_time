from django.test import TestCase
from .models import User
from django.db.models import Manager

# class UserMethodTestCase(TestCase):
#     def setUp(self):
        #   self.first_name = "jen"
        #   self.last_name = "bel"
#         pass

# test cases for registration() function in the model  
    # 1. self.assertEqual() --> True when a user is added successfully
    # 2. self.assertEqual() --> False when a field for user will be empty

# test cases for getCoffee() function in the model  
    # 1. True case when the result id is not equal to user id
    # 2. True when the length of result will be only 1
    # 3. Returns a message recommending get lunch when user has met with everyone
   

# test for getLunch() function in the model
    # 1. Check that length of lunch group range is between 3 and 5
    # 2. Check when it has less than 3 user in the system. Lunch group length will equal to 2

   
# test for addLunchFriend() function in the model  
    # 1. True when a friend is added to user.lunch_friends
    # 2. False when not added
   