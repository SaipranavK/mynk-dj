from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from alerts.models import Alert
from category.models import Category
from expense_log.models import ExpenseLog
from reports.models import Report

from datetime import date

@login_required(login_url = 'accounts:authenticate')
def dashboard_root(request):
    
    date_today = date.today()
    days_this_month = 0
    
    if date_today.month%2 == 0 or date_today != 2 or date_today != 8:
        days_this_month = 30
    
    elif date_today.month == 8:
        days_this_month = 31

    elif date_today.month == 2:
        if date_today.year % 4 == 0:
            if date_today.year % 100 == 0:
                if date_today.year % 400 == 0:
                    days_this_month = 29
                else:
                    days_this_month = 28
            else:
                days_this_month = 29
        else:
            days_this_month = 28

    
    print("Checking Date:", date_today.day)
    if date_today.day == 1 :
        print("Generating report")
        userCheck = Q(user = request.user)
        prev_month = date_today.month - 1
        periodCheck = Q(period = date_today.replace(month=prev_month))
        if Report.objects.filter(userCheck & periodCheck).exists():
            pass
        else:
            return redirect("reports:generate")

    monthly_limit = request.user.profile.monthly_limit - request.user.profile.monthly_savings
    categories = Category.objects.filter(user = request.user)
    expenseLogs = ExpenseLog.objects.filter(user = request.user, date__range=(date_today.replace(day=1), date_today.replace(day=days_this_month))).order_by('-date')
    
    spent = remaining = 0
    for category in categories:
        spent += category.this_month

    today = 0
    for expense in expenseLogs:
        if expense.date == date_today:
            today += expense.amount

    remaining = monthly_limit - spent
    time_delta = date_today - date_today.replace(day=1)
    daily_average = int(spent/ (time_delta.days+1)) 

    if daily_average > (monthly_limit/30):
        recommendation = "You are overspending"
        recommendation_message = "You should spend under " + str(int(monthly_limit/30)) + " SEK/day to avoid going over your monthly budget" 
        recommendation_badge = "badge-danger"
    
    else:
        recommendation = "All Good"
        recommendation_message = "You are spending under " + str(int(monthly_limit/30)) + " SEK/day. Keep managing your expenses to stay within your monthly budget" 
        recommendation_badge = "badge-success"

    alerts = Alert.objects.filter(user = request.user)

    context = {
        'alerts': alerts,
        'monthly_limit': monthly_limit,
        'categories': categories,
        'expenseLogs': expenseLogs,
        'spent': spent,
        'remaining': remaining,
        'today': today,
        'daily_average': daily_average,
        'recommendation': recommendation,
        'recommendation_message': recommendation_message,
        'recommendation_badge': recommendation_badge
    }

    return render(request, "dashboard/dashboard.html", context)

def category_chart_data(request):
    
    categories = Category.objects.filter(user = request.user)
    
    data = []
    tempBlock = []

    for category in categories:
        tempBlock.append(category.name)
        tempBlock.append(category.this_month)
        data.append(tempBlock)
        tempBlock = []
        
    chart = {
        'chart': {'type': 'pie', 'height': 310},
        'title': {'text': ''},
        'series': [{
            'name': 'Category Expense distribution',
            'data': data
        }]
    }

    return JsonResponse(chart)

