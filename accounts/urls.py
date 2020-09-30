from django.urls import path

from .views import login_view, logout_view, register_view, account_setup, edit_profile

app_name = "accounts"

urlpatterns = [
    path('authenticate/', login_view, name = "authenticate"),
    path('logout/', logout_view, name = "logout"),
    path('register/', register_view, name = "register"),
    path('setup/', account_setup, name = "setup"),
    path('edit/', edit_profile, name = "edit"),
]