from django import forms
from .models import ExpenseLog

class ExpenseLogForm(forms.ModelForm):
    class Meta:
        model = ExpenseLog
        exclude = ('user', )