from django.test import TestCase
from django.contrib.auth.models import User

from .models import Profile

import datetime

class AccountsLogModelTest(TestCase):

    def setUpTestData():
        user = User.objects.create(username = "testuser", password = "test@12345")
        profile = Profile.objects.create(user = user, monthly_limit = 10000, monthly_savings = 1000)
        
    def test_AccountsDB(self):
        
        User_record = User.objects.get(username = "testuser")
        Profile_record = Profile.objects.get(user = User_record)
        
        #assertion 
        self.assertEqual(User_record.username, "testuser")
        self.assertEqual(Profile_record.user.username, "testuser")
        

