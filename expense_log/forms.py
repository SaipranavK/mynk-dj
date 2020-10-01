from django import forms
from .models import ExpenseLog

from category.models import Category

class ExpenseLogForm(forms.ModelForm):
    class Meta:
        model = ExpenseLog
        exclude = ('user', )