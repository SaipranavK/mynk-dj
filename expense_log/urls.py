from django.urls import path
from . import views

app_name = "expence_log"

urlpatterns = [
    path('create_log/', views.create_log , name = "create_log"),
    path('update_log/', views.update_log , name = "update_log"),
    #path('create_log/', create_log , name = "create_log"),

]