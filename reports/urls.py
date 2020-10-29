from django.urls import path

from .views import reports_root,  report_details, report_chart_data, generate_report

app_name = "reports"

urlpatterns = [
    path("", reports_root, name = "root"),
    path("generate/", generate_report, name = "generate"),
    path("details/<int:report_id>/", report_details, name = "details"),
    path("chart-data/<int:report_id>/", report_chart_data, name = "category-chart-data")
]