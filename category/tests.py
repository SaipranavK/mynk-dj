from django.test import TestCase
from django.contrib.auth.models import User

from .models import Category

from accounts.models import Profile

import datetime

class CategoryModelTest(TestCase):

    def setUpTestData():
        user = User.objects.create(username = "testuser", password = "test@12345")
        profile = Profile.objects.create(user = user, monthly_limit = 10000, monthly_savings = 1000)
        category = Category.objects.create(user = user, name = "Test Category", value = 3000)

    def test_categoryDB(self):
        
        User_record = User.objects.get(username = "testuser")
        Profile_record = Profile.objects.get(user = User_record)
        Category_record = Category.objects.get(user = User_record, name = "Test Category")
       
        #assertion 
        self.assertEqual(User_record.username, "testuser")
        self.assertEqual(Profile_record.user.username, "testuser")
        self.assertEqual(Category_record.user.username, "testuser")
        self.assertEqual(Category_record.name, "Test Category")
        

