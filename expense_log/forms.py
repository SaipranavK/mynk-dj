from django import forms
from .models import ExpenseLog

from category.models import Category

class DateInput(forms.DateInput):
    input_type = 'date'

class ExpenseLogForm(forms.ModelForm):
    class Meta:
        model = ExpenseLog
        exclude = ('user', )
        widgets = {
            'date': DateInput(),
        }