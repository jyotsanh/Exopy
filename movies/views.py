#   Movies   URL

from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

@login_required
def movies(request):
    if request.method == 'POST':
        None
    else:
        return render(request,"movies.html")