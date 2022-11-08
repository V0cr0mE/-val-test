from fastapi.testclient import TestClient
from main import app
client = TestClient(app)


def test_create_trainer():
    """
        test route post /trainer/
    """
    response = client.post(
        '/trainers/',
        json= { "name": "trainer1", "birthdate": "2000-10-20" }
    )
    assert response.status_code == 200
    assert response.json()['name'] == "trainer1"
    assert response.json()['birthdate'] == "2000-10-20"

def test_get_trainers():
    """
        test route get /trainers/
    """
    response = client.get('/trainers')
    assert response.status_code == 200
    assert isinstance(response.json()) == isinstance([])

def test_get_trainer():
    """
        test route get /trainers/{id_trainer}
    """
    response = client.get('/trainers/1')
    assert response.status_code == 200
    assert response.json()['id'] == 1

def test_post_item_trainer():
    """
        test route post /trainers/{id_trainer}/item/
    """
    response = client.post(
        'trainers/1/item/',
        json= {"name": "potion", "description": "heal 10 hp"}
    )
    assert response.status_code == 200
    assert response.json()['name'] == "potion"
    assert response.json()['description'] == "heal 10 hp"
    assert response.json()['trainer_id'] == 1

def test_post_pokemon_trainer():
    """
        test route post /trainers/{id_trainer}/pokemon/
    """
    response = client.post(
        'trainers/1/pokemon/',
        json= {"api_id": 1, "custom_name": "pokemon1"}
    )
    assert response.status_code == 200
    assert response.json()['api_id'] == 1
    assert response.json()['custom_name'] == "pokemon1"
    assert response.json()['trainer_id'] == 1
    assert response.json()['name'] == "bulbasaur"

def test_get_items():
    """
        test route get /itms/
    """
    response = client.get('/items/')
    assert response.status_code == 200
    assert isinstance(response.json()) == isinstance([])

def test_get_pokemons():
    """
        test route get /pokemons/
    """
    response = client.get('/pokemons/')
    assert response.status_code == 200
    assert isinstance(response.json()) == isinstance([])

def test_get_combat():
    """
        test route post /combat/{id_first_pokemon}/{id_second_pokemon}
    """
    response = client.get('/combat/1/2')
    assert response.status_code == 200
