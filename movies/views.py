#   Movies   URL
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
import time

import requests



def greet():
    current_time = time.localtime()
    hour = current_time.tm_hour
    gre = ""
    if hour < 12:
        gre = "Good Morning"
    elif hour < 18:
        gre = "Good Afternoon"
    else:
        gre = "Good Evening"
    return gre

    
@login_required
def home(request):
    if request.method == 'POST':
        pass
    else:

        username = request.session.get('username')
        password1 = request.session.get('password')
        user = authenticate(username=username,password=password1)
        
        if user is not None:
            login(request,user)
            # return render(request,"movies.html")
            prompt = greet()
            data = {
                "name":username,
                "greet":prompt
                }
            return render(request,"movies.html",data)
        else:
           
            messages.error(request,"Please provide a valid username and password")
            return redirect('accounts:dash')
        



def logout(request):

    logout(request)
    request.session.clear()
    return redirect("accounts:dash")
