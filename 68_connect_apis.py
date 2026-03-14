import requests

base_url = "https://pokeapi.co/api/v2/"


try:
    def get_pokemon_info(name):
        url = f"{base_url}/pokemon/pikachu"
        response = requests.get(url)

    pokemon_name = "pikachu"
    get_pokemon_info(pokemon_name)
except requests.exceptions.SSLError:
    print("Your college wifi SUCKS")
