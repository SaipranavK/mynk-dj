from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Profile
from .forms import ProfileForm

from category.models import Category

def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard:root")
    
    if request.method == "POST":
        authForm = AuthenticationForm(data = request.POST)
        if authForm.is_valid():
            user = authForm.get_user()
            login(request,user)

            if Profile.objects.filter(user = user).exists():
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('dashboard:root')
            else:
                return redirect('accounts:setup')

    else:
        authForm = AuthenticationForm()

    return render(request,"accounts/authenticate.html", {'authForm': authForm})


def logout_view(request):
    logout(request)
    return redirect('accounts:authenticate')

def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard:root")

    if request.method == "POST":
        regForm = UserCreationForm(data = request.POST)

        if regForm.is_valid():
            regForm.save()
            username = regForm.cleaned_data.get('username')
            raw_password = regForm.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("accounts:setup")
        
    else:
        regForm = UserCreationForm()

    return render(request, "accounts/register.html", {"regForm": regForm})

@login_required(login_url = 'accounts:authenticate')
def account_setup(request):
    if Profile.objects.filter(user = request.user).exists():
        return redirect('dashboard:root')

    if request.method == 'POST':
        profileForm = ProfileForm(request.POST, request.FILES)
        if profileForm.is_valid():
            instance = profileForm.save(commit = False)
            instance.user = request.user
            
            if instance.monthly_limit < instance.monthly_savings:
                messages.warning(request, f"Monthly savings cannot be greater than your monthly expense limit")
                return redirect('accounts:setup')

            instance.save()
            return redirect('dashboard:root')
    else:
        profileForm = ProfileForm()

    return render(request, "accounts/setup.html", {"profileForm": profileForm})

@login_required(login_url = 'accounts:authenticate')
def edit_profile(request):
    user = request.user 
    if request.method == 'POST':
        
        categories = Category.objects.filter(user = user)
        category_sum = 0
        for category in categories:
            category_sum += category.value
        
        profileForm = ProfileForm(request.POST, request.FILES, instance = user.profile)
        if(profileForm.is_valid()):
            instance = profileForm.save(commit = False)

            if instance.monthly_limit < instance.monthly_savings:
                messages.warning(request, f"Monthly savings cannot be greater than your monthly expense limit")
                return redirect('accounts:edit')

            if instance.monthly_limit - instance.monthly_savings < category_sum:
                messages.warning(request, f"Your category wise expense limits are greater than your monthly expense limit. Please adjust category limits before changing your monthly expense limit")
                return redirect('accounts:edit')

            instance.save()
            messages.warning(request, f"Account information updated")
            
    else:
        profileForm = ProfileForm(instance = user.profile)

    return render(request, "accounts/edit.html", {'profileForm':profileForm})






