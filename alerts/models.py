from django.db import models
from django.contrib.auth.models import User

from category.models import Category

class Alert(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    limit = models.PositiveIntegerField(default = 10, verbose_name = "Limit", help_text = "Amount at which the alert should be triggered")
    alert_message = models.CharField(max_length = 64,blank = True, null = True)

    def __str__(self):
        return str(self.user)+ " | "+ str(self.category)