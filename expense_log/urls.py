from django.urls import path
from . import views

app_name = "expense_log"

urlpatterns = [
    path('create/', views.create_log , name = "create"),
    path('update/<int:id>/', views.update_log , name = "edit"),
    path('delete-confirm/<int:id>/', views.delete_confirm_log , name = "delete-confirm"),
    path('delete/<int:id>/', views.delete_log , name = "delete"),
]