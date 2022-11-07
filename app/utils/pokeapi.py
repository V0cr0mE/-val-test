"""
    Pokemon and battle actions
"""

import requests

BASE_URL = "https://pokeapi.co/api/v2"


def get_pokemon_name(api_id):
    """
        Get a pokemon name from the API pokeapi
    """
    return get_pokemon_data(api_id)['name']

def get_pokemon_stats(api_id):
    """
        Get pokemon stats from the API pokeapi
    """
    return get_pokemon_data(api_id)["stats"]

def get_pokemon_data(api_id):
    """
        Get data of pokemon name from the API pokeapi
    """
    return requests.get(f"{BASE_URL}/pokemon/{api_id}", timeout=10).json()


def battle_pokemon(pokemon_api_id: int, pokemon2_api_id: int) -> dict[str, int]:
    """
        Do battle between 2 pokemons
        Params:
            pokemonApiID (int): id of the first pokemon
            pokemon2ApiID (int): id of the second pokemon
        Return:
            {"pokemonApiID":pokemonApiID, "result": resultValue:int} (None if draw)
    """
    premier_pokemon = get_pokemon_data(pokemon_api_id)
    second_pokemon = get_pokemon_data(pokemon2_api_id)
    battle_result = battle_compare_stats(premier_pokemon["stats"], second_pokemon["stats"])
    if battle_result > 0:
        return {"pokemonApiID":pokemon_api_id, "result": battle_result}
    if battle_result < 0:
        return {"pokemonApiID":pokemon2_api_id, "result": battle_result}
    return {"pokemon":None, "result": battle_result}


def battle_compare_stats(first_pokemon_stats, second_pokemon_stats) -> float:
    """
        Compare given stat between two pokemons
    """
    result = 0
    for i, stats in enumerate(first_pokemon_stats):
        result += stats["base_stat"] - second_pokemon_stats[i]["base_stat"]
    return result
