#   ACCOUNT URL

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

from django.core.mail import EmailMessage, send_mail
from Exopy import settings
from django.template import loader


def dash(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password']
        user = authenticate(username=username, password=password1)

        if user is not None:

            login(request, user)
            request.session['username'] = username
            request.session['password'] = password1
            return redirect('movies:home')
        else:
            messages.error(request, "Invalid username or password")
            return render(request, 'dash.html')

    else:
        request.session.clear()
        return render(request, "dash.html")


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
            messages.error(request, "username already exist")
            return redirect('/')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('/')

        if len(username) > 20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('/')

        if password1 != password2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('/')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('/')

        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = firstname
        myuser.last_name = lastname

        myuser.save()

        return redirect('/')

    else:
        return render(request, "register.html")

