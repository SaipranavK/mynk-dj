from django.db import models
from django.contrib.auth.models import User

from category.models import Category

class Report(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    period = models.DateField()
    total_exp = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return str(self.user) + " | " + str(self.period)

    def get_period(self):
        month_dict = {1: 'Janaury', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
        display_str = month_dict[self.period.month]
        display_str += ", " + str(self.period.year)

        return display_str

class CategorySnap(models.Model):

    report = models.ForeignKey(Report, on_delete = models.CASCADE)
    category = models.CharField(max_length = 128)
    spent = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return str(self.report) + " | " + str(self.category)


