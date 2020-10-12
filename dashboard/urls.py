from django.urls import path
from .views import dashboard_root, category_chart_data

app_name = "dashboard"

urlpatterns = [
    path('', dashboard_root, name = "root"), 
    path('category-chart/data/', category_chart_data, name = "category-chart-data")
]