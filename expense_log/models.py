from django.db import models
from django.contrib.auth.models import User

class ExpenseLog(models.Model):
    user = models.ForeignKey('User', on_delete = models.CASCADE)
    amount = models.PositiveIntegerField(default = 0)
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(max_length=512)

    def __str__(self):
        return str(self.user) + "|" + str(self.date)
