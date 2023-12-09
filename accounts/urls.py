from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("",views.dash,name="dash"),
    path("register/", views.register, name="register"),
    path("forgot/", views.forgot, name="forgot"),
    # Add more URL patterns for account-related views
]
