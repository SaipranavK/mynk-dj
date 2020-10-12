from django.urls import path
from .views import alerts_root, create_alert, edit_alert

app_name = "alerts"

urlpatterns = [
    path('', alerts_root, name = "root"),
    path('create/', create_alert, name = "create"),
    path('edit/<int:alert_id>/', edit_alert, name = "edit")
]