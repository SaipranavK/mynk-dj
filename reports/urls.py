from django.urls import path

from .views import reports_root, generate_report, report_details

app_name = "reports"

urlpatterns = [
    path("", reports_root, name = "root"),
    path("generate/", generate_report, name = "generate"),
    path("details/<int:report_id>", report_details, name = "details")
]