#   ACCOUNT URL

from django.shortcuts import render,redirect

def bash(request):
    if request.method == 'POST':
        None
    else:
        return render(request,"./templates/dash.html")