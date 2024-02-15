#   ACCOUNT URL
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.mail import EmailMessage, send_mail
from Exopy import settings
from django.template import loader
import random



def generate_code():
    return str(random.randint(100000, 999999))

def send_code_to_user(email, code):
    send_mail(
        'Your verification code',
        f'Your verification code is {code}',
        'thanksbro6969@gmail.com',  # Replace with your email
        [email],
        fail_silently=False,
    )


def dash(request):
    if request.method == 'POST':
        try:
            
            username = request.POST['username']
            password1 = request.POST['password']
            firstname = request.POST.get('firstname', False)
            if firstname:
                raise ValueError("Invalid input value.")
            else:
                user = authenticate(username=username, password=password1)

                if user is not None:

                    login(request, user)
                    request.session['username'] = username
                    request.session['password'] = password1
                    return redirect('movies:home')
                else:
                    messages.error(request, "Invalid username or password")
                    return render(request, 'dash.html')
        except:
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
            try:
                messages.success(request, "User Successfully saved.")
                myuser.save()
            except:
                messages.error(request, "User is not saved.")
                return render(request, 'dash.html')
            
        return redirect('/')

    else:
        request.session.clear()
        return render(request, "dash.html")


def forgot(request):
    if request.method == 'POST':
        username = request.POST['username']  # Replace with the name of your username field
        email = request.POST['email']
        try:
            user = User.objects.get(username=username, email=email)
        except User.DoesNotExist:
            # Handle the case where the user does not exist
            
            return render(request, "forgot.html", {"error": "User with provided username and email does not exist."})

        # If the user exists, generate and send the code
        try:
            code = generate_code()
            send_code_to_user(email, code)
            
        except Exception as e:
            
             return render(request, "excuse.html", {"error": f"Something error happend during sending mail {e}"})
        return render(request,"excuse.html",{"error": "Email Sent successfully"})
        
    else:
        return render(request,"forgot.html")

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

