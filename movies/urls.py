from django.urls import  path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Other URL patterns
    path("",views.movies,name="movies"),
]