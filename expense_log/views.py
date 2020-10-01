from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#local import
from .models import ExpenseLog 
from . import models
from .forms import ExpenseLogForm
from django.contrib.auth.models import User

# Create your views here.

#Create
@login_required(login_url = 'accounts:authenticate')
def create_log(request):
    if request.method == 'POST':
        expenseLogForm =ExpenseLogForm(request.POST)
        ####expenseLogForm.user = request.user
        if expenseLogForm.is_valid():
            #####
            expenseLogForm.save()
        return redirect('dashboard:root')
    else:
        expenseLogForm =ExpenseLogForm()
        return render(request, "expense_log/create_log.html", {"expenseLogForm":expenseLogForm})

#read
@login_required(login_url = 'accounts:authenticate')
def read_log(request):

    return True

#update
@login_required(login_url = 'accounts:authenticate')
def update_log(request):
    if request.method == 'POST':
        ####expenseLogForm =ExpenseLogForm(request.POST,instance = user.profile)
        if expenseLogForm.is_valid():
            instance.save()
        return redirect('dashboard:root')
    else:
        ####expenseLogForm =ExpenseLogForm()
        return render(request, "expense_log/update_log.html", {"expenseLogForm":expenseLogForm})


