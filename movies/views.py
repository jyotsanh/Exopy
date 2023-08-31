#   Movies   URL
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
import time

import requests

base_url = "https://image.tmdb.org/t/p/w500"
api_key = "201dadbac9d90432aa44713682a9eb60"

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



def trend():
    url = f"https://api.themoviedb.org/3/trending/movie/week?api_key={api_key}"

    response = requests.get(url)
    data = response.json()
    return data
    
def genre(g_id):
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={g_id}'
    response = requests.get(url)
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
            request.session['username'] = username
            request.session['password'] = password1
            datas = trend()
            
            
            # -----------------------------------------------------------------
            movies_title = []
            movies_url = []
            id = []
            
            for movie in datas["results"]:
                movies_title.append(movie["title"])
                movies_url.append(base_url + movie['poster_path'])
                id.append(movie['id'])
            # ------------------------------------------------------------------
            action_data = genre(28)
            # action
            a_titles = []
            a_url = []
            a_id = []
            for movie in action_data['results']:
                a_titles.append(movie['title'])
                a_id.append(movie['id'])
                a_url.append(base_url+movie['poster_path'])
            
            # ----------------------------------------------------------------------
            # fantasy
            Fantsay_data = genre(14)
            f_titles = []
            f_url = []
            f_id = []
            for movie in Fantsay_data['results']:
                f_titles.append(movie['title'])
                f_id.append(movie['id'])
                f_url.append(base_url+movie['poster_path'])
            data = {
                "movie":movies_title,
                'url':movies_url,
                'g_title':a_titles,
                'g_url':a_url,
                'g_id':a_id,
                'id':id,
                
                "name":username,
                'f_title':f_titles,
                'f_url':f_url,
                'f_id':f_id,
                'num_range': range(len(movies_title))
                }
            return render(request,"movies.html",data)
        else:
           
            messages.error(request,"Please provide a valid username and password")
            return redirect('accounts:dash')
        

def info(request):
    if request.method == 'POST':
        pass
    else:

        
        id = request.GET.get('id')
    
        movie_url = f'https://api.themoviedb.org/3/movie/{id}?api_key={api_key}'
        movie_response = requests.get(movie_url)
        movie_data = movie_response.json()

        # Extract the desired information from the movie_data object
        movie_name = movie_data['title']
        posture_url = base_url + movie_data['poster_path']
        watch_time = movie_data['runtime']
        rating = movie_data['vote_average']
        description = movie_data['overview']
        genres = [genre['name'] for genre in movie_data['genres']]
        genres = ', '.join(genres)
        credits_url = f'https://api.themoviedb.org/3/movie/{id}/credits?api_key={api_key}'
        credits_response = requests.get(credits_url)
        credits_data = credits_response.json()
        cast = [actor['name'] for actor in credits_data['cast']]
        crew = [member['name'] for member in credits_data['crew']]
        cast = ', '.join(cast)
        crew = ', '.join(crew)
        data = { 
            'title':movie_name,
            'url':posture_url,
            'watch_time':watch_time,
            'rating':rating,
            'description':description,
            'genres':genres,
            'cast':cast,
            'crew':crew,
             }
    return render(request,"info.html",data)


def genre_movies(request):
    if request.method == 'POST':
        # Handle POST request logic if needed
        pass
    else:
        genre_id = request.GET.get('gid')
        
        data = genre(genre_id)
        genres = request.GET.get('name')
        g_title = []
        g_url = []
        g_id = []
        for movie in data['results']:
            g_title.append(movie['title'])
            g_id.append(movie['id'])
            g_url.append(base_url+movie['poster_path'])
        data = {
                "movie":g_title,
                'url':g_url,
                'genre':genres,
                
                
                "g_id":g_id,
                'num_range': range(len(g_title))
                }
        return render(request,"genre.html",data)


# views.py



def logout(request):

    logout(request)
    request.session.clear()
    return redirect("accounts:dash")
