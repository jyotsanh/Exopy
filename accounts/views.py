#   ACCOUNT URL

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.mail import EmailMessage, send_mail
from Exopy import settings

def dash(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password']
        user = authenticate(username=username,password=password1)
        
        if user is not None:

            login(request,user)
            
            return redirect('/movies/?fname={}'.format(username))
        else:
            messages.error(request, "Invalid username or password")
            return render(request,"dash.html")

    else:
        return render(request,"dash.html")
    
def logout_view(request):

    logout(request)
    return redirect("dash")

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirmpassword']

        if User.objects.filter(username=username):
            messages.error(request,"username already exist")
            return redirect('dash')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('dash')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('dash')
        
        if password1 != password2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('dash')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('dash')
        myuser = User.objects.create_user(username,email,password1)
        myuser.first_name = firstname
        myuser.last_name = lastname

        myuser.save()

        return redirect('dash') 
        
    else:
        return render(request,"register.html")


    
def home(request):
    None