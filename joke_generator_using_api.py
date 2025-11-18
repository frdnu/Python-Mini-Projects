import requests
import random

url = 'https://icanhazdadjoke.com/search'
count = 0
user_input = input('Want kind of joke you want? : ')

while True:
    response = requests.get(
        url, headers={"accept": "application/json"}, params={'term': user_input}).json()
    jokes = [x["joke"] for x in response["results"]]

    no_of_jokes = len(jokes)
    if no_of_jokes > 0:
        print(
            f"We found {no_of_jokes} jokes about {user_input}\nOne of them is: {random.choice(jokes)}\n")
    else:
        print('No jokes found Sorry :(\n')

    user_input = input('Want kind of joke you want? (Enter Q to stop) : ')

    if user_input == 'q' or user_input == 'Q':
        break
