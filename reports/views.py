from django.shortcuts import render,redirect
from django.db.models import Sum
from django.contrib import messages

from .models import Report, CategorySnap
from category.models import Category
from expense_log.models import ExpenseLog

from datetime import date

def reports_root(request):

    reports = Report.objects.filter(user = request.user)
    return render(request, "reports/root.html", {"reports":reports})

def generate_report(request):

    prev_month = date.today().month - 1
    total_exp = Category.objects.aggregate(Sum('this_month'))
    report = Report.objects.create(user = request.user, period = date.today().replace(month = prev_month), total_exp = total_exp['this_month__sum'])
    
    categories = Category.objects.filter(user = request.user)
    for category in categories:
        CategorySnap.objects.create(report = report, category = category.name, spent = category.this_month)
        category.this_month = 0
        category.save()

    return redirect("dashboard:root")

def report_details(request, report_id):

    try:
        report = Report.objects.get(id = report_id)
        categorySnaps = CategorySnap.objects.filter(report = report)

        no_days = 0
    
        if report.period.month % 2 == 0 or report.period.month != 2 or report.period.month != 8:
            no_days = 30
        
        elif report.period.month == 8:
            no_days = 31

        elif report.period.month == 2:
            if report.period.year % 4 == 0:
                if report.period.year % 100 == 0:
                    if report.period.year % 400 == 0:
                        no_days = 29
                    else:
                        no_days = 28
                else:
                    no_days = 29
            else:
                no_days = 28

        expenseLogs = ExpenseLog.objects.filter(user = request.user, date__range=(report.period.replace(day=1), report.period.replace(day = no_days))).order_by('-date')
        return render(request,"reports/details.html", {'report': report, 'categorySnaps': categorySnaps, 'expenseLogs': expenseLogs})

    except:
        messages.warning(request,f"Unable to fetch requested report from your profile")
        return redirect("reports:root")

    