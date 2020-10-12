from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 32, verbose_name = "Category Name")
    value = models.PositiveIntegerField(default = 0, verbose_name = "Category Limit", help_text = "Maximum spending in this category from total monthly expense")
    this_month = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return self.name

    def calc_progress_percent(self):
        return (self.this_month/self.value)*100

    def get_progress_color(self):
        value = Category.calc_progress_percent(self)
        if value < 50:
            return "bg-info"
        elif value > 50 and value < 70:
            return "bg-warning"
        elif value > 70:
            return "bg-danger"


