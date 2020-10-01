from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'defaults/avatar.png', upload_to = "profile_pics/", verbose_name = "Avatar")
    monthly_limit = models.PositiveIntegerField(default = 1000, help_text = "SEK/month", verbose_name = "Monthly Expense Limit")

    def __str__(self):
        return str(self.user)