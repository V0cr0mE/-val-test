from http import client
from urllib import response
from fastapi.testclient import TestClient
import pytest
from main import app
client = TestClient(app)


####################################
#           MOCK TESTS             #
####################################


#Test 1
def test_pokemon_battle(mocker):
    mocker.patch(
        "app.utils.pokeapi.battle_compare_stats",
        return_value = 1
    )
    
    first_poke_api_id=1
    second_poke_api_id=4

    response = client.get(f"/pokemons/battle?first_poke_api_id={first_poke_api_id}&second_poke_api_id={second_poke_api_id}")
    result = {"winner": "bulbasaur"}
    assert result == response.json()
    assert response.status_code == 200

#Test 2
def test_trainer_item(mocker):
    mocker.patch(
        "",
        return_value = ""
    )


#Test 3
def test_get_three_random_pokemon(mocker, mocker2):
    pass
    mocker.patch(
        "app.utils.pokeapi.get_pokemon_name",
        return_value = {"name": "cottonee"}
    )

    mocker2.patch(
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
        assert poke['name'] == "cottonee"
        assert poke['stats'] == {"hp": 40, "attack": 27, "defense": 60, "special-attack": 37, "special-defense": 50, "speed": 66}
    
    assert response.status_code == 200
    


#Test 4
def test4(mocker):
    pass
    mocker.patch(
        "",
        return_value = ""
    )


#Test 5
def test5(mocker):
    pass
    mocker.patch(
        "",
        return_value = ""
    )