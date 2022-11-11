from http import client
from urllib import response
from fastapi.testclient import TestClient
import pytest
from main import app
client = TestClient(app)


####################################
#           MOCK TESTS             #
####################################


# Test 1
# Check the pokemon/battle endpoint : winner
def test_pokemon_battle_win(mocker):
    mocker.patch(
        "app.utils.pokeapi.battle_compare_stats",
        return_value = 1
    )
    
    first_poke_api_id=1
    second_poke_api_id=4

    response = client.get(f"/pokemons/battle?first_poke_api_id={first_poke_api_id}&second_poke_api_id={second_poke_api_id}")
    assert response.status_code == 200
    assert response.json() == {"winner": "bulbasaur"}
    

# Test 2
# Check the pokemon/battle endpoint : draw
def test_pokemon_battle_draw(mocker):
    mocker.patch(
        "app.utils.pokeapi.battle_compare_stats",
        return_value = 0
    )

    first_poke_api_id=1
    second_poke_api_id=1

    response = client.get(f"/pokemons/battle?first_poke_api_id={first_poke_api_id}&second_poke_api_id={second_poke_api_id}")
    assert response.status_code == 200
    assert response.json() == {'winner': 'draw'} 


# Test 3
# Check if the get_three_random_pokemon endpoint return 3 pokemons with the right format
def test_get_three_random_pokemon(mocker):
    pass
    mocker.patch(
        "app.utils.pokeapi.get_pokemon_name",
        return_value = {"name": "cottonee"}
    )

    mocker.patch(
        "app.utils.pokeapi.get_pokemon_stats",
        return_value = {"hp": 40,
                        "attack": 27,
                        "defense": 60,
                        "special-attack": 37,
                        "special-defense": 50,
                        "speed": 66}
    )

    response = client.get("/pokemons/random")
    assert len(response.json()) > 0 

    for poke in response.json():
        assert poke['name'] == {"name": "cottonee"}
        assert poke['stats'] == {"hp": 40, "attack": 27, "defense": 60, "special-attack": 37, "special-defense": 50, "speed": 66}
    
    assert response.status_code == 200
    

# # Test 4
# # Check
# def test_none_pokemon_for_trainer(mocker):
#     """
#         Creation d'un pokemon inexistant
#     """
#     mocker.patch(
#         "app.utils.pokeapi.get_pokemon_name", 
#         return_value=None
#         )

#     response = client.post("/trainers/1/pokemon/", json={"api_id": 0,"custom_name": "string"})
#     assert response.status_code == 500
#     assert response.json() == {"detail": "Pokemon not found"}


# Test 5
# def test5(mocker):
#     pass
#     mocker.patch(
#         "",
#         return_value = ""
#     )