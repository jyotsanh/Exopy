from django.urls import  path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'movies'

urlpatterns = [
    # Other URL patterns
    path("home/",views.home,name="home"),
    path("logout/",views.logout,name='logout'),
    path("info/",views.info,name="info")
]