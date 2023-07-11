#   Movies   URL
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout

@login_required
def home(request):
    if request.method == 'POST':
        pass
    else:
        username = 'lek'
        password1 =  'lek2'
        user = authenticate(username=username,password=password1)
        
        if user is not None:
            login(request,user)
            # return render(request,"movies.html")
            
            return render(request,"movies.html")
        else:
           
            messages.error(request,"Please provide a valid username and password")
            return redirect('accounts:dash')
        
def logout(request):

    logout(request)
    return redirect("accounts:dash")
