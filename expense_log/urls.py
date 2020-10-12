from django.urls import path
from . import views

app_name = "expense_log"

urlpatterns = [
    path('create/', views.create_log , name = "create"),
    path('update/<int:id>', views.update_log , name = "edit"),
]