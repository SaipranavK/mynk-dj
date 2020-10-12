from django.test import TestCase
from django.contrib.auth.models import User

from .models import ExpenseLog

from accounts.models import Profile
from category.models import Category

import datetime

class ExpenseLogModelTest(TestCase):

    def setUpTestData():
        user = User.objects.create(username = "testuser", password = "test@12345")
        profile = Profile.objects.create(user = user, monthly_limit = 10000, monthly_savings = 1000)
        category = Category.objects.create(user = user, name = "Test Category", value = 3000)
        expenselog = ExpenseLog.objects.create(user = user, category = category, amount = 1000, date = datetime.date.today(), notes = "Test notes")


    def test_ExpenseLogDB(self):
        
        User_record = User.objects.get(username = "testuser")
        Profile_record = Profile.objects.get(user = User_record)
        Category_record = Category.objects.get(user = User_record, name = "Test Category")
        ExpenseLog_record = ExpenseLog.objects.get(user = User_record, category = Category_record, amount=1000)
        #assertion 
        self.assertEqual(User_record.username, "testuser")
        self.assertEqual(Profile_record.user.username, "testuser")
        self.assertEqual(Category_record.user.username, "testuser")
        self.assertEqual(Category_record.name, "Test Category")
        self.assertEqual(ExpenseLog_record.amount, 1000)
        
