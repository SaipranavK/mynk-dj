from django.db import models
from django.contrib.auth.models import User

from category.models import Category

class Report(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    period = models.DateField()
    total_exp = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return str(self.user) + " | " + str(self.period)

class CategorySnap(models.Model):

    report = models.ForeignKey(Report, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    spent = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return str(self.report) + " | " + str(self.category)

