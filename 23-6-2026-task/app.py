# dependant function to be tested

import requests

def get_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    return response.json()