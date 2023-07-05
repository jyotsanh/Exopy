#   ACCOUNT URL

from django.shortcuts import render,redirect

def dash(request):
    if request.method == 'POST':
        None
    else:
        return render(request,"./templates/dash.html")