import requests

def fetch_user(username):
    response = requests.get(f'https://api.github.com/users/{username}')
    return response.json()

def search_users(query):
    response = requests.get(f'https://api.github.com/search/users?q={query}')
    return response.json()['items']
