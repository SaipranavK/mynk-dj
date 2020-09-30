from django.urls import path
from .views import dashboard_root

app_name = "dashboard"

urlpatterns = [
    path('', dashboard_root, name = "root"),
]