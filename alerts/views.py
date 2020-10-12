from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .models import Alert
from .forms import AlertForm

from category.models import Category

@login_required(login_url = 'accounts:authenticate')
def alerts_root(request):
    alerts = Alert.objects.filter(user = request.user)
    return render(request, "alerts/root.html", {"alerts": alerts})

@login_required(login_url = 'accounts:authenticate')
def create_alert(request):
    if request.method == "POST":
        alertForm = AlertForm(request.POST)
        if alertForm.is_valid():
            instance = alertForm.save(commit = False)
            instance.user = request.user

            userCheck = Q(user = request.user)
            categoryCheck = Q(category = instance.category)


            if Alert.objects.filter(userCheck & categoryCheck).exists():
                messages.warning(request, f'Alert for this category already exists')
                return redirect("alerts:root")

            
            category = instance.category
            
            if category.value < instance.limit:
                messages.warning(request, f"Alert cannot be triggered at a value greater than category limit")
                return redirect("alerts:root")

            instance.save()
            messages.warning(request, f"Alert has been created")
            return redirect("alerts:root")

    else:
        alertForm = AlertForm()

    return render(request, "alerts/add.html", {"alertForm": alertForm})

@login_required(login_url = 'accounts:authenticate')
def edit_alert(request, alert_id):

    alert = Alert.objects.get(id = alert_id)

    if request.method == "POST":
        alertForm = AlertForm(request.POST, instance = alert)
        if alertForm.is_valid():
            instance = alertForm.save(commit = False)

            category = instance.category
            if category.value < instance.limit:
                messages.warning(request, f"Alert cannot be triggered at a value greater than category limit")
                return redirect("alerts:root")

            instance.save()
            messages.warning(request, f"Alert has been updated")
            return redirect("alerts:root")

    else:
        alertForm = AlertForm(instance = alert)

    return render(request, "alerts/add.html", {"alertForm": alertForm})
