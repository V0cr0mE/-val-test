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
    pokemon = get_pokemon_data(api_id)
    
    pokemon_stats = {
            pokemon["stats"][0]["stat"]["name"]: pokemon["stats"][0]["base_stat"],
            pokemon["stats"][1]["stat"]["name"]: pokemon["stats"][0]["base_stat"],
            pokemon["stats"][2]["stat"]["name"]: pokemon["stats"][0]["base_stat"],
            pokemon["stats"][3]["stat"]["name"]: pokemon["stats"][0]["base_stat"],
            pokemon["stats"][4]["stat"]["name"]: pokemon["stats"][0]["base_stat"],
            pokemon["stats"][5]["stat"]["name"]: pokemon["stats"][0]["base_stat"]
    }
    return pokemon_stats

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
    premierPokemonData = get_pokemon_stats(first_api_id)
    secondPokemonData = get_pokemon_stats(second_api_id)
    battle_result = battle_compare_stats(premierPokemonData,secondPokemonData)
    return premierPokemon if battle_result > 0 else secondPokemon if battle_result < 0 else {'winner': 'draw'}
    

def battle_compare_stats(first_pokemon_stats, second_pokemon_stats):
    """
        Compare given stat between two pokemons
    """
    battle_result = 0
    for keys in first_pokemon_stats:
        if(first_pokemon_stats[keys] > second_pokemon_stats[keys]):
            battle_result += 1
        elif(first_pokemon_stats[keys] == second_pokemon_stats[keys]):
            battle_result == 0
        else:
            battle_result -= 1
    return battle_result
