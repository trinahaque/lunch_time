from django.test import TestCase
from .models import User
from django.db.models import Manager

# class UserMethodTestCase(TestCase):
#     def setUp(self):
#         pass
#     def test_getCoffee(self):
#         users = User.objects.all()
#         if len(users) > 0:
#             id = 1
#         else:
#             id = 0
#         user = User.objects.get(id=id)
#         self.assertNotEqual(User.objects.getCoffee(pid=id), id)