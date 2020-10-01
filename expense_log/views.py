from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
#local import
from .models import ExpenseLog 
from . import models
from .forms import ExpenseLogForm
from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.

#Create
@login_required(login_url = 'accounts:authenticate')
def create_log(request):
    if request.method == 'POST':
        expenseLogForm =ExpenseLogForm(request.POST)
        ####expenseLogForm.user = request.user
        if expenseLogForm.is_valid():
            #####
            instance = expenseLogForm.save(commit=False)
            instance.user=request.user
            instance.save()
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
def update_log(request,id):
    userCheck = Q(user = request.user)
    expensecheck = Q(pk = id)

    print("trying.................")
    #user1 = ExpenseLog.objects.get(userCheck)
    user1 = ExpenseLog.objects.get(userCheck & expensecheck)  
   
    #this code still not work corectly and instead of update it just add new row  as expensecheck = Q(pk = id) will be key of table not specific to user may be database need more clearence 
    #except:
        #messages.success("Unable to fetch requested user profile")
    #   return redirect("dashboard:root")
    

    if request.method == 'POST':
        expenseLogForm =ExpenseLogForm(request.POST,instance = user1)
        if expenseLogForm.is_valid():
            expenseLogForm.save()
            return redirect('dashboard:root')
    else:
        expenseLogForm =ExpenseLogForm(instance = user1)
        ##getting multiple instances of expenseLogForm of a single user
        return render(request, "expense_log/update_log.html", {"expenseLogForm":expenseLogForm})


