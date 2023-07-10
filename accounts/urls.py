from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("",views.dash,name="dash"),
    path("register/", views.register, name="register"),
    path("acc",views.logout,name="logout")
    # Add more URL patterns for account-related views
]
