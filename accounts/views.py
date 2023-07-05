#   ACCOUNT URL

from django.shortcuts import render,redirect

def dash(request):
    if request.method == 'POST':
        None
    else:
        return render(request,"dash.html")
    

# Create your views here.
def register(request):
    if request.method == 'POST':
        None
    else:
        return render(request,"register.html")

def login(request):
    if request.method == "POST":
        None
    else:
        return render(request,"login.html")
    