from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Category
from .forms import CategoryForm

@login_required(login_url = 'accounts:authenticate')
def add_category(request):
    if request.method == "POST":
        catForm = CategoryForm(request.POST)
        if catForm.is_valid():
            instance = catForm.save(commit = False)
            categories = Category.objects.filter(user = request.user)
            sum = 0
            for category in categories:
                sum += category.value
            
            sum += instance.value
            
            if(sum >= request.user.profile.monthly_limit):
                messages.warning(request,f'Exceeding Monthly Expense limit')
                return redirect("dashboard:root")

            instance = catForm.save(commit = False)
            instance.user = request.user
            instance.save()

            return redirect("dashboard:root")

    else:
        catForm = CategoryForm()

    return render(request, "category/add.html", {"catForm": catForm})


@login_required(login_url = 'accounts:authenticate')
def edit_category(request, category_name):

        
    userCheck = Q(user = request.user)
    categoryCheck = Q(name = category_name)


    try:
        category = Category.objects.get(userCheck & categoryCheck)    
    

    except:
        messages.success("Unable to fetch requested category in your profile")
        return redirect("dashboard:root")
    

    if request.method == "POST":
        catForm = CategoryForm(request.POST, instance = category)

        if catForm.is_valid():
            catForm.save()

            messages.success(request, f"Category Updated")
            return redirect("dashboard:root")
        
    else:
        catForm = CategoryForm(instance = category)

    return render(request, "category/edit.html", {"catForm": catForm})

    
@login_required(login_url = 'accounts:authenticate')
def delete_confirm_category(request, category_name):

    userCheck = Q(user = request.user)
    categoryCheck = Q(name = category_name)


    try:
        category = Category.objects.get(userCheck & categoryCheck)    
    

    except:
        messages.success("Unable to fetch requested category in your profile")
        return redirect("dashboard:root")
    

    return render(request, "category/delete-confirm.html", {"category": category})

    
@login_required(login_url = 'accounts:authenticate')
def delete_category(request, category_name):

    userCheck = Q(user = request.user)
    categoryCheck = Q(name = category_name)


    try:
        category = Category.objects.get(userCheck & categoryCheck)    
    

    except:
        messages.success("Unable to fetch requested category in your profile")
        return redirect("dashboard:root")

    category.delete()

    messages.success(request, f"Category deleted from your profile")
    return redirect("dashboard:root")

    
