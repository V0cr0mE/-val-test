from fastapi.testclient import TestClient
from main import app
from app.utils.pokeapi import get_pokemon_data, battle_pokemon
client = TestClient(app)

base_url = "https://pokeapi.co/api/v2"
def test_getPokemons():
    response = client.get("/pokemons")
    assert response.status_code == 200

def test_getPokemon_id():
    """
       get one Pokemon
    """
    api_id = 1
    response = get_pokemon_data(api_id)
    result = "bulbasaur"
    assert reponse["name"] == result

def test_battlePokemon_vainqueur():
    """
        battle with pokemon_id_1 and pokemon_id_2
    """
    pokemon_id_1 = 1
    pokemon_id_2 = 2
    response = battle_pokemon(1,2)
    result = "ivysaur"
    assert response == result
