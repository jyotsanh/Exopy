import requests
api_key = "201dadbac9d90432aa44713682a9eb60"
id = 872585
movie_url = f'https://api.themoviedb.org/3/movie/{id}?api_key={api_key}'
movie_response = requests.get(movie_url)
movie_data = movie_response.json()


print("---------------------------------------------------------")


def genre(g_id, max_pages=5):
    api_key = 'YOUR_API_KEY'  # Replace with your actual API key
    all_data = []

    for page in range(1, max_pages + 1):
        url = f'https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={g_id}&page={page}'
        response = requests.get(url)
        data = response.json()
        all_data.extend(data['result'])

    return all_data



action_data = genre(14)
print(action_data)
for movie in action_data['results']:
    print(movie['title'])
