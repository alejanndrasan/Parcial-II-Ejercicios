from tools import *
from Pokemon import Pokemon
import random

def main():
    #Fetching Json:
    pokemon_list = make_request('https://pokeapi.co/api/v2/pokemon-form')
    random.shuffle(pokemon_list)

    #Menu:
    print('')
