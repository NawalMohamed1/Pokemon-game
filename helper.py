import requests
import random


def get_random_pokemon_selection(): # function that will get 5 pokemon names
    random_numbers = random.sample(range(1, 150), 5)
    random_pokemon = []
    for number in random_numbers:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{number}")
        pokemon = response.json()
        random_pokemon.append(pokemon["name"])
    return random_pokemon


def get_pokemon_info(name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
    pokemon = response.json()
    return pokemon