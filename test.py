import requests
api_key = "201dadbac9d90432aa44713682a9eb60"
id = 872585
movie_url = f'https://api.themoviedb.org/3/movie/{id}?api_key={api_key}'
movie_response = requests.get(movie_url)
movie_data = movie_response.json()


print("---------------------------------------------------------")

print(movie_data['original_title'])
print(movie_data['runtime'])
print(movie_data['popularity'])
print(movie_data['revenue'])
for i in movie_data['spoken_languages']:
    for j in i:
        print(j.value)
print(movie_data['vote_count'])
