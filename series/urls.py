from django.urls import  path
from . import views
urlpatterns = [
    # Other URL patterns
    path("",views.bash,name="bash"),
    path("info",views.info,name="info"),
]