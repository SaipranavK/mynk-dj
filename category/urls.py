from django.urls import path
from .views import add_category

app_name = "category"

urlpatterns = [
    path('add/', add_category, name = "add")
]