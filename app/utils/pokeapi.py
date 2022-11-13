import requests

base_url = "https://pokeapi.co/api/v2"


def get_pokemon_name(api_id):
    """
        Get a pokemon name from the API pokeapi
    """
    return get_pokemon_data(api_id)['name']

def get_pokemon_stats(api_id):
    """
        Get pokemon stats from the pokeapi API
    """
    #Nous avons choisi que 4 stats par pokemon
    pokemon_data = get_pokemon_data(api_id)

    stats = {
        pokemon_data["stats"][0]["stat"]["name"]: pokemon_data["stats"][0]["base_stat"],  #HP
        pokemon_data["stats"][1]["stat"]["name"]: pokemon_data["stats"][0]["base_stat"],  #Attack
        pokemon_data["stats"][2]["stat"]["name"]: pokemon_data["stats"][0]["base_stat"],  #Defense
        pokemon_data["stats"][5]["stat"]["name"]: pokemon_data["stats"][0]["base_stat"]    #Speed
    }

    return stats

def get_pokemon_data(api_id):
    """
        Get data of pokemon name from the API pokeapi
    """
    return requests.get(f"{base_url}/pokemon/{api_id}", timeout=10).json()


def battle_pokemon(first_api_id, second_api_id):
    """
        Do battle between 2 pokemons
    """

    firstPokemon = get_pokemon_data(first_api_id)
    secondPokemon = get_pokemon_data(second_api_id)
    battle_result = battle_compare_stats(firstPokemon, secondPokemon)

    return (f"The winner is {firstPokemon} !" if battle_result > 0
    else f"The winner is {secondPokemon} !" if battle_result < 0
    else {'winner': 'draw'})


def battle_compare_stats(first_pokemon_stats, second_pokemon_stats):
    """
        Compare given stats between 2 pokemons
    """
    result = 0

    stats_p1 = get_pokemon_stats(first_pokemon_stats)
    stats_p2 = get_pokemon_stats(second_pokemon_stats)

    for stat in stats_p1:
        if stats_p1[stat] > stats_p2[stat]:
            result += 1
        elif stats_p1[stat] < stats_p2[stat]:
            result -= 1
        else: continue
    return result
