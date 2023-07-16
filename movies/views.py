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

base_url = "https://image.tmdb.org/t/p/w500"
api_key = "201dadbac9d90432aa44713682a9eb60"

def trend():
    url = f"https://api.themoviedb.org/3/trending/movie/week?api_key={api_key}"

    response = requests.get(url)
    data = response.json()
    return data
    
def series():
    url = f'https://api.themoviedb.org/3/trending/tv/day?api_key={api_key}'

    # Send a GET request to the API endpoint
    response = requests.get(url)

    # Parse the JSON response data
    data = response.json() 
    return data

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
            datas = series()
            movies_title = []
            movies_url = []
            for movie in datas["results"]:
                movies_title.append(movie["name"])
                movies_url.append(base_url + movie['poster_path'])
            prompt = greet()
            data = {
                "movie":movies_title,
                'url':movies_url,
                "name":username,
                "greet":prompt,
                'num_range': range(len(movies_title))
                }
            return render(request,"movies.html",data)
        else:
           
            messages.error(request,"Please provide a valid username and password")
            return redirect('accounts:dash')
        



def logout(request):

    logout(request)
    request.session.clear()
    return redirect("accounts:dash")
