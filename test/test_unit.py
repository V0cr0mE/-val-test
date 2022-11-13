from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_pokemons():
    """
        Recuperation de la liste des pokemons
    """
    response = client.get("/pokemons")
    assert response.status_code == 200
    assert response.json()[0] == {"api_id": 3,"custom_name": "TestPokemon","id": 1,"name": "venusaur","trainer_id": 2}

def test_pokemon_battle():
    """
        Test de la fonction de combat
    """
    response = client.get("/pokemons/battle/2/6")
    assert response.status_code == 200
    assert response.json() == 6

def test_pokemon_battle_draw():
    """
        Test de la fonction de combat si egalite
    """
    response = client.get("/pokemons/battle/2/2")
    assert response.status_code == 200
    assert response.json() == {'winner': 'draw'}
def test_get_items():
    """
        Recuperation de la liste des items
    """
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json()[1] == {"name": "GodMod","description": "100% WinRate","id": 2,"trainer_id": 2}

def test_get_trainer():
    """
        Recuperation de la liste des Trainers
    """
    response = client.get("trainers/1")
    assert response.status_code == 200
    assert response.json() == {"name": "balou", "birthdate": "2012-11-07", "id":1, "inventory": [], "pokemons": []}