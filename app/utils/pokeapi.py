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
    stats =  get_pokemon_data(api_id)['stats']
    stat_pokemon = 0
    for stat in stats:
        stat_pokemon += stat['base_stat']
    return stat_pokemon

def get_pokemon_data(api_id):
    """
        Get data of pokemon name from the API pokeapi
    """
    return requests.get(f"{base_url}/pokemon/{api_id}", timeout=10).json()


def battle_pokemon(first_pokemon, second_pokemon):
    """
        Do battle between 2 pokemons
    """
    battle_result = battle_compare_stats(get_pokemon_stats(first_pokemon.api_id), get_pokemon_stats(second_pokemon.api_id))
    return first_pokemon if battle_result > 0 else second_pokemon if battle_result < 0 else {'winner': 'draw'}


def battle_compare_stats(first_pokemon_stats, second_pokemon_stats):
    """
        Compare given stat between two pokemons
    """
    return first_pokemon_stats - second_pokemon_stats
