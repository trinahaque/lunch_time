from django.test import TestCase
from .models import User
from django.db.models import Manager

# class UserMethodTestCase(TestCase):
#     def setUp(self):
        #   self.first_name = "jen"
        #   self.last_name = "bel"
#         pass

# test cases for registration() function in the model 
    # User1 --> fields for first_name and last_name are fully filled out
    # User2 --> fields are empty
    # 1. self.assertEqual() --> True when a user is added successfully
    # 2. self.assertEqual() --> False when a field for user will be empty

# test cases for getCoffee() function in the model  
    # Add two users to the function. One is user, other is user2
    # 1. First test case will try to find id of the first coffee friend. 
    # True case when the result id is not equal to user id
    # 2. True when the function will return only one user (length check test case)
    # 3. Add two users to the function. Call the function again. Returns an error
    #  message recommending get lunch when user has met with everyone
   

# test for getLunch() function in the model
    # Add only two users
    # 1. True when the length of lunch group is 2
    # Add over four users. Call the getLunch() function to generate a group.
    # True when the length of lunch group range is between 3 and 5
    
 
# test for addLunchFriend() function in the model  
    # 1. True when a friend is added to user.lunch_friends
    # 2. False when not added
   