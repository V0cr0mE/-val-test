"""
use api
"""
import requests

BASE_URL = "https://pokeapi.co/api/v2"


def get_pokemon_name(api_id):
    """
        Get a pokemon name from the API pokeapi
    """
    return get_pokemon_data(api_id)['name']

def get_pokemon_stats():
    """
        Get pokemon stats from the API pokeapi
    """
    return False

def get_pokemon_data(api_id):
    """
        Get data of pokemon name from the API pokeapi
    """
    return requests.get(f"{BASE_URL}/pokemon/{api_id}", timeout=10).json()


def battle_pokemon(first_api_id, second_api_id):
    """
        Do battle between 2 pokemons
    """
    premier_pokemon = get_pokemon_data(first_api_id)
    second_pokemon = get_pokemon_data(second_api_id)
    battle_result = battle_compare_stats(premier_pokemon["stats"],second_pokemon["stats"])
    if battle_result > 0:
        return premier_pokemon["id"]
    if battle_result < 0:
        return second_pokemon["id"]
    return {'winner': 'draw'}


def battle_compare_stats(first_pokemon_stats, second_pokemon_stats):
    """
        Compare given stat between two pokemons
    """
    result = 0

    result += first_pokemon_stats[0]["base_stat"]-second_pokemon_stats[0]["base_stat"]
    result += first_pokemon_stats[1]["base_stat"]-second_pokemon_stats[1]["base_stat"]
    result += first_pokemon_stats[2]["base_stat"]-second_pokemon_stats[2]["base_stat"]
    result += first_pokemon_stats[3]["base_stat"]-second_pokemon_stats[3]["base_stat"]
    result += first_pokemon_stats[4]["base_stat"]-second_pokemon_stats[4]["base_stat"]
    result += first_pokemon_stats[5]["base_stat"]-second_pokemon_stats[5]["base_stat"]

    return result
