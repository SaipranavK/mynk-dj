from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 32, verbose_name = "Category Name")
    value = models.PositiveIntegerField(default = 0, verbose_name = "Category Limit", help_text = "Maximum spending in this category from total monthly expense")

    def __str__(self):
        return str(self.user) + " | " + self.name

