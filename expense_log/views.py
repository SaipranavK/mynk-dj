from django.shortcuts import render , redirect
from django.contrib import messages
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
        prev_amount = ex_log.amount

        if request.user == ex_log.user:
            if request.method == 'POST':
            
                expenseLogForm = ExpenseLogForm(request.POST, request.FILES, instance = ex_log)
                print(expenseLogForm)
                if expenseLogForm.is_valid():
                    
                    instance = expenseLogForm.save(commit = False)
                    category = instance.category

                    print("Current: ", category.this_month)
                    print("Ex_log amount:", prev_amount)
                    category.this_month -= prev_amount
                    print("minus:", category.this_month)
                    print("Instance amount:", instance.amount)
                    category.this_month += instance.amount
                    print("new:", category.this_month)

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
                expenseLogForm = ExpenseLogForm(instance = ex_log)
                
            expenseLogForm.fields["category"].queryset= Category.objects.filter(user = request.user)
                
            return render(request, "expense_log/edit.html", {"expenseLogForm":expenseLogForm})  

    except:
        messages.success(request, f"Unable to fetch requested expense log from your profile")
        return redirect("dashboard:root")
    
    
@login_required(login_url = 'accounts:authenticate')
def delete_confirm_log(request, id):

    try:
        ex_log = ExpenseLog.objects.get(pk = id)
        if request.user == ex_log.user:
            return render(request, "expense_log/delete-confirm.html", {"expense": ex_log})

    except:
        messages.success(request, f"Unable to fetch requested Expense Log from your profile")
        return redirect("dashboard:root")
    

@login_required(login_url = 'accounts:authenticate')
def delete_log(request, id):

    try:
        ex_log = ExpenseLog.objects.get(pk = id)
        if request.user == ex_log.user:
            
            category = ex_log.category
            category.this_month -= ex_log.amount
            category.save()
            ex_log.delete()

            userCheck = Q(user = request.user)
            categoryCheck = Q(category = category)
            alert = Alert.objects.get(userCheck & categoryCheck)
            
            if category.this_month >= alert.limit:
                if alert.alert_message == None:
                    alert.alert_message = "You have crossed your alert limit for "+ category.name +" this month. Be careful while spending to avoid going your budget"
                    
            else:
                if alert.alert_message:
                    alert.alert_message = None

            alert.save()         
            
            messages.success(request, f"Expense Log deleted from your profile")
            return redirect("dashboard:root") 
    
    except:
        messages.success(request, f"Unable to fetch requested expense log from your profile")
        return redirect("dashboard:root")