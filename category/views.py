from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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



