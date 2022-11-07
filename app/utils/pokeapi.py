import requests

base_url = "https://pokeapi.co/api/v2"


def get_pokemon_name(api_id):
    """
        Get a pokemon name from the API pokeapi
    """
    return get_pokemon_data(api_id)['name']


def get_pokemon_stats(api_id):
    """
        Get pokemon stats from the API pokeapi
    """
    return False


def get_pokemon_data(api_id):
    """
        Get data of pokemon name from the API pokeapi
    """
    return requests.get(f"{base_url}/pokemon/{api_id}", timeout=10).json()


def battle_pokemon(first_api_id, second_api_id):
    """
        Do battle between 2 pokemons
        return the name of the pokemon winner
    """
    premierPokemon = get_pokemon_data(first_api_id)
    secondPokemon = get_pokemon_data(second_api_id)
    pokemon_1 = {"name": premierPokemon["forms"][0]['name'], "health": premierPokemon['stats'][0]['base_stat'],
                 "attack": premierPokemon['stats'][1]['base_stat']}
    pokemon_2 = {"name": secondPokemon["forms"][0]['name'], "health": secondPokemon['stats'][0]['base_stat'],
                 "attack": secondPokemon['stats'][1]['base_stat']}

    while True:
        pokemon_1['health'] = pokemon_1['health'] - pokemon_2['attack']
        if (pokemon_1['health'] <= 0):
            return pokemon_2['name']
        pokemon_2['health'] = pokemon_2['health'] - pokemon_1['attack']
        if (pokemon_2['health'] <= 0):
            return pokemon_1['name']


def battle_compare_stats(first_pokemon_stats, second_pokemon_stats):
    """
        Compare given stat between two pokemons
    """
