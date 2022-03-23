import requests
from Pokemon import Pokemon

#Validaciones:


#Fetch json and turn it into objects:

def make_request(url):
    response = requests.get(url)
    cont = 0
    
    #Fetching json:
    if response.status_code == 200:
        pokemons = []
        payload = response.json()

    #Turning it into objecs:
    for pokemon in payload.get("results"):
        cont+=1
        pokemon_object = Pokemon("","", cont)
        for key, value in pokemon.items():
            if key == "name":
                pokemon_object.name = value
            elif key == 'url': 
                pokemon_object.url = value
            else:
                pokemon_object.spot = cont

        pokemons.append(pokemon_object)
     
    return pokemons

#Methods:

def selection_sort(lista): 
    long = len(lista)

    for i in range(long-1):
        menor = i
        for j in range(i+1, long):
            if lista[menor].spot>lista[j].spot:
                menor = j
        temp = lista[i].spot
        lista[i].spot=lista[menor].spot
        lista[menor].spot=temp

def busqueda_por_puesto(lista, value_to_find):
    for item in lista:
        if item.spot == value_to_find:
            return item.spot, item.name, item.url
    return 'El elemento que busca no se encuentra en la lista'


def busqueda_por_nombre(lista, value_to_find):
    for item in lista:
        if item.nombre == value_to_find:
            return item.spot, item.name, item.url
    return 'El elemento que busca no se encuentra en la lista'












        