#   Movies   URL

from django.shortcuts import render,redirect

def movies(request):
    if request.method == 'POST':
        None
    else:
        return render(request,"movies.html")