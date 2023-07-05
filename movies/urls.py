from django.urls import  path
from . import views

urlpatterns = [
    # Other URL patterns
    path("",views.movies,name="movies"),
]