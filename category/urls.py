from django.urls import path
from .views import add_category, edit_category, delete_confirm_category, delete_category

app_name = "category"

urlpatterns = [
    path('add/', add_category, name = "add"),
    path('edit/<str:category_name>', edit_category, name = "edit"),
    path('delete-confirm/<str:category_name>', delete_confirm_category, name = "delete-confirm"),
    path('delete/<str:category_name>', delete_category, name = "delete")
]