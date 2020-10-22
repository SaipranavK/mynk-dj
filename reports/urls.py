from django.urls import path

from .views import reports_root

app_name = "reports"

urlpatterns = [
    path("", reports_root, name = "root")
]