from django.shortcuts import render

def dashboard_root(request):
    return render(request, "dashboard/dashboard.html")