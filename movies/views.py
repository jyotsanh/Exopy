#   Movies   URL
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout

@login_required
def movies(request):
    if request.method == 'POST':
        None
    else:
        username = request.GET.get('fname')
        
        if User.objects.filter(username=username):

            # return render(request,"movies.html")
            
            return render(request,"movies.html",{"fname":username})
        else:
           
            messages.error(request,"Please provide a valid username and password")
            return redirect('accounts:dash')
        
def logout(request):

    logout(request)
    return redirect("accounts:dash")
