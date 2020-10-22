from django.shortcuts import render

from .models import Report

def reports_root(request):
    reports = Report.objects.filter(user = request.user)
    return render(request, "reports/root.html", {"reports":reports})

