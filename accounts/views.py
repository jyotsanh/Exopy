#   ACCOUNT URL

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect

def dash(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password']
        user = authenticate(username=username,password=password1)
        if user is not None:

            login(request,user)
            return redirect("movies")
        else:
            messages.error(request, "Invalid username or password")
            return render(request,"dash.html")

    else:
        return render(request,"dash.html")
    

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirmpassword']
        myuser = User.objects.create_user(username,email,password1)
        myuser.first_name = firstname
        myuser.last_name = lastname

        myuser.save()

        messages.success(request,"Your Account is succesfully Created")

        return redirect(reverse("accounts:dash")) 
        
    else:
        return render(request,"register.html")


    
def home(request):
    None