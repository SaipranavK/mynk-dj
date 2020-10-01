from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q

#local import
from .models import ExpenseLog 
from . import models
from .forms import ExpenseLogForm

from category.models import Category


@login_required(login_url = 'accounts:authenticate')
def create_log(request):
    if request.method == 'POST':
        expenseLogForm =ExpenseLogForm(request.POST)    
        if expenseLogForm.is_valid():
            instance = expenseLogForm.save(commit=False)
            instance.user=request.user
            instance.save()
            
            return redirect('dashboard:root')
    else:
        expenseLogForm =ExpenseLogForm()
        
    expenseLogForm.fields["category"].queryset= Category.objects.filter(user = request.user)
    
    return render(request, "expense_log/create.html", {"expenseLogForm":expenseLogForm})

@login_required(login_url = 'accounts:authenticate')
def update_log(request,id):    
    try:
        ex_log = ExpenseLog.objects.get(pk = id)  

    except:
        messages.success("Unable to fetch requested expense log from your profile")
        return redirect("dashboard:root")
   
    #this code still not work corectly and instead of update it just add new row  as expensecheck = Q(pk = id) will be key of table not specific to user may be database need more clearence 
    #except:
        #messages.success("Unable to fetch requested user profile")
    #   return redirect("dashboard:root")
    
    if request.method == 'POST':
        expenseLogForm =ExpenseLogForm(request.POST, instance = ex_log)
        if expenseLogForm.is_valid():
            expenseLogForm.save()
            return redirect('dashboard:root')
    
    else:
        expenseLogForm =ExpenseLogForm(instance = ex_log)
        ##getting multiple instances of expenseLogForm of a single user

    expenseLogForm.fields["category"].queryset= Category.objects.filter(user = request.user)
        
    return render(request, "expense_log/edit.html", {"expenseLogForm":expenseLogForm})


