from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from category.models import Category

@login_required(login_url = 'accounts:authenticate')
def dashboard_root(request):

    categories = Category.objects.filter(user = request.user)

    context = {
        'categories': categories,
        'cat_spent_per': 73, 
        'cat_spent': 1300
    }

    return render(request, "dashboard/dashboard.html", context)