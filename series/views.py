#   series URL
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

def series():
    url = f'https://api.themoviedb.org/3/trending/tv/day?api_key={api_key}'

    # Send a GET request to the API endpoint
    response = requests.get(url)

    # Parse the JSON response data
    data = response.json() 
    return data

def bash(request):
    if request.method == 'POST':
        None
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
            id=[]
            for movie in datas["results"]:
                movies_title.append(movie["name"])
                movies_url.append(base_url + movie['poster_path'])
                id.append(movie['id'])
            prompt = greet()
            data = {
                "movie":movies_title,
                'url':movies_url,
                "name":username,
                "id":id,
                "greet":prompt,
                'num_range': range(len(movies_title))
                }
            return render(request,"joma.html",data)
        else:
           
            messages.error(request,"Please provide a valid username and password")
            return redirect('accounts:dash')
        


def info(request):
    if request.method == "POST":
        None
    else:
        id = request.GET.get('id')
        tv_url = f'https://api.themoviedb.org/3/tv/{id}?api_key={api_key}'
        tv_response = requests.get(tv_url)
        tv_data = tv_response.json()

        name = tv_data['name']
        tv_url = base_url+tv_data['poster_path']
        description = tv_data['overview']
        try:
            tv_time = tv_data['episode_run_time'][0]
        except:
            tv_time = 'not fixed'
        rating = tv_data['vote_average']
        genres = [genre['name'] for genre in tv_data['genres']]
        genres = ', '.join(genres)
        url = f"https://api.themoviedb.org/3/tv/{id}?api_key={api_key}&append_to_response=credits"
        response = requests.get(url)
        tv_show_data = response.json()

        director = ""
        cast = []
        crew = tv_data.get('credits', {}).get('crew', [])
    
    # Find the director's name based on their job
        director = next((person['name'] for person in crew if person['job'] == 'Director'), None)

        for cast_member in tv_show_data['credits']['cast'][:3]:
            cast.append(cast_member['name'])
        cast = ", ".join(cast)
        data = {
           'name':name,
           'url':tv_url,
           'time':tv_time,
           'dir':director,
           'cast':cast,
           'rating':rating,
           'desc':description,
           'genre':genres 
            }
        return render(request,"info_series.html",data)
        