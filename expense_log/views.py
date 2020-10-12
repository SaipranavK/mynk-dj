from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q

#local import
from .models import ExpenseLog 
from . import models
from .forms import ExpenseLogForm

from category.models import Category
from alerts.models import Alert

@login_required(login_url = 'accounts:authenticate')
def create_log(request):
    if request.method == 'POST':
        expenseLogForm =ExpenseLogForm(request.POST, request.FILES)   
        print(expenseLogForm) 
        if expenseLogForm.is_valid():
            instance = expenseLogForm.save(commit=False)
            instance.user=request.user
            
            category = instance.category
            category.this_month += instance.amount

            try:
                userCheck = Q(user = request.user)
                categoryCheck = Q(category = category)
                alert = Alert.objects.get(userCheck & categoryCheck)
                if category.this_month >= alert.limit:
                    alert.alert_message = "You have crossed your alert limit for "+ category.name +" this month. Be careful while spending to avoid going your budget"
                    alert.save() 
            except:
                pass

            category.save()
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
    
    if request.method == 'POST':
        expenseLogForm =ExpenseLogForm(request.FILES, request.POST, instance = ex_log)
        if expenseLogForm.is_valid():
            instance = expenseLogForm.save(commit = False)

            try:
                category = instance.category
                userCheck = Q(user = request.user)
                categoryCheck = Q(category = category)
                alert = Alert.objects.get(userCheck & categoryCheck)
                if category.this_month >= alert.limit:
                    alert.alert_message = "You have crossed your alert limit for "+ category.name +" this month. Be careful while spending to avoid going your budget"
                    alert.save() 
            except:
                pass
            
            return redirect('dashboard:root')
    
    else:
        expenseLogForm =ExpenseLogForm(instance = ex_log)
        ##getting multiple instances of expenseLogForm of a single user

    expenseLogForm.fields["category"].queryset= Category.objects.filter(user = request.user)
        
    return render(request, "expense_log/edit.html", {"expenseLogForm":expenseLogForm})

