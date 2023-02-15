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
    return get_pokemon_data(api_id)['stats']

def get_pokemon_data(api_id):
    """
        Get data of pokemon name from the API pokeapi
    """
    return requests.get(f"{base_url}/pokemon/{api_id}", timeout=10).json()


def battle_pokemon(first_api_id, second_api_id):
    """
        Do battle between 2 pokemons
    """
    premierPokemon = get_pokemon_data(first_api_id)
    secondPokemon = get_pokemon_data(second_api_id)
    battle_result = battle_compare_stats(first_api_id, second_api_id)
    return premierPokemon if battle_result > 0 else secondPokemon if battle_result < 0 else {'winner': 'draw'}


def battle_compare_stats(first_pokemon_stats, second_pokemon_stats):
    """
        Compare given stat between two pokemons
    """
    chalenger_1 = get_pokemon_stats(first_pokemon_stats)
    chalenger_2 = get_pokemon_stats(second_pokemon_stats)
    
    chalenger_1_points = 0
    chalenger_2_points = 0
    count = 0
    
    for stat in chalenger_1:
        if stat["base_stat"] > chalenger_2[count]["base_stat"]:
            chalenger_1_points += 1
            count += 1
        elif stat["base_stat"] < chalenger_2[count]["base_stat"]:
            chalenger_2_points += 1
            count += 1
        else:
            count += 1
            
    if chalenger_1_points > chalenger_2_points:
        return 1
    elif chalenger_1_points < chalenger_2_points:
        return -1
    else:
        return 0
