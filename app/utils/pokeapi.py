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


def battle_pokemon(pokemon_1, pokemon_2):
    """
        Do battle between 2 pokemons
        return the name of the pokemon winner
    """
    premier_pokemon = get_pokemon_data(pokemon_1.api_id)
    second_pokemon = get_pokemon_data(pokemon_2.api_id)

    compteur_1 = 0
    compteur_2 = 0

    for i in range(min(len(premier_pokemon['stats']), len(second_pokemon['stats']))):
        if(premier_pokemon['stats'][i]['base_stat']>second_pokemon['stats'][i]['base_stat']):
            compteur_1+=1
        elif (premier_pokemon['stats'][i]['base_stat']==second_pokemon['stats'][i]['base_stat']):
            pass
        else:
            compteur_2+=1

    return premier_pokemon["forms"][0]['name'] if compteur_1>=compteur_2 else second_pokemon["forms"][0]['name']


def battle_compare_stats(first_pokemon_stats, second_pokemon_stats):
    """
        Compare given stat between two pokemons
    """
