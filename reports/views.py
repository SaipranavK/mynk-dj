from django.http import JsonResponse
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

def report_chart_data(request, report_id):
    try:
        report = Report.objects.get(id = report_id)
        categories = CategorySnap.objects.filter(report = report)

    
        data = []
        tempBlock = []

        for snap in categories:
            tempBlock.append(snap.category)
            tempBlock.append(snap.spent)
            data.append(tempBlock)
            tempBlock = []
            
        chart = {
            'chart': {'type': 'pie', 'height': 295},
            'title': {'text': ''},
            'series': [{
                'name': 'Category Expense distribution',
                'data': data
            }]
        }

        return JsonResponse(chart)

    except:
        return JsonResponse({'message': 'Unable to fetch data'})



def generate_report(request):

    date_today = date.today()
    prev_month = 0
    prev_month_days = 0
    prev_month_year = 0

    if date_today.month != 1:
        prev_month = date_today.month - 1
    else:
        prev_month = 12

    if prev_month == 12:
        prev_month_year = date_today.year - 1
    else:
        prev_month_year = date_today.year

    if prev_month%2 == 0 or prev_month != 2 or prev_month != 8:
        prev_month_days = 30
    
    elif prev_month == 8:
        prev_month_days = 31

    elif prev_month == 2:
        if prev_month_year % 4 == 0:
            if prev_month_year % 100 == 0:
                if prev_month_year % 400 == 0:
                    prev_month_days = 29
                else:
                    prev_month_days = 28
            else:
                prev_month_days = 29
        else:
            prev_month_days = 28

    
     
    total_exp = Category.objects.aggregate(Sum('this_month'))
    daily_avg = total_exp/prev_month_days
    savings = total_exp - request.user.profile.monthly_limit + request.user.profile.monthly_savings

    report = Report.objects.create(user = request.user, period = date.today().replace(month = prev_month), total_exp = total_exp['this_month__sum'], daily_avg =  daily_avg, savings = savings)
    
    categories = Category.objects.filter(user = request.user)
    for category in categories:
        CategorySnap.objects.create(report = report, category = category.name, spent = category.this_month)
        category.this_month = 0
        category.save()

    return redirect("dashboard:root")



    