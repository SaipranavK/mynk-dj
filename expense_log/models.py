from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

from category.models import Category

class ExpenseLog(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    amount = models.FloatField(default = 0, validators=[MinValueValidator(0)])
    date = models.DateField()
    attachment = models.FileField(blank = True, null = True, upload_to = "attachments/")
    notes = models.TextField(max_length=512)

    def __str__(self):
        return str(self.user) + "|" + str(self.date)
