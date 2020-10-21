from django.urls import path
from .views import alerts_root, create_alert, edit_alert, delete_confirm_alert, delete_alert

app_name = "alerts"

urlpatterns = [
    path('', alerts_root, name = "root"),
    path('create/', create_alert, name = "create"),
    path('edit/<int:alert_id>/', edit_alert, name = "edit"),
    path('delete-confirm/<int:alert_id>/', delete_confirm_alert, name = "delete-confirm"),
    path('delete/<int:alert_id>/', delete_alert, name = "delete")
]