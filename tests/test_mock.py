from fastapi.testclient import TestClient
from main import app
from app import models

client = TestClient(app)


def test_get_trainers(mocker):
    """
        test MOCK route get /trainers/{id_trainer}
    """
    model = models.Trainer(name='trainer1', birthdate='2022-11-07', id=1)
    mocker.patch(
        "app.routers.trainers.actions.get_trainer",
        return_value=model
    )
    response = client.get("/trainers/1")
    assert 'trainer1' == response.json()['name']
    assert '2022-11-07' == response.json()['birthdate']
    assert response.status_code == 200

def test_create_item_for_trainer(mocker):
    """
        test MOCK route post /trainers/{id_trainer}/item/
    """
    model = models.Item(name='potion', description='heal 10 pv', id=100, trainer_id=1)
    mocker.patch(
        "app.routers.trainers.actions.add_trainer_item",
        return_value=model
    )
    response = client.post(
        "/trainers/1/item/",
        json= {"name": "potion", "description": "heal 10 hp"}
    )
    assert response.status_code == 200
    assert 'potion' == response.json()['name']
    assert 'heal 10 pv' == response.json()['description']
    assert 1 == response.json()['trainer_id']

def test_create_pokemon_for_trainer(mocker):
    """
        test MOCK route post /trainers/{id_trainer}/pokemon
    """
    model = models.Pokemon(
        name = 'wigglytuff',
        api_id = 40,
        id = 100,
        trainer_id = 1,
        custom_name = "poketest"
    )
    mocker.patch(
        "app.routers.trainers.actions.add_trainer_pokemon",
        return_value=model
    )
    response = client.post(
        "/trainers/1/pokemon/",
        json= {"api_id": 100, "custom_name": "poketest"}
    )
    assert response.status_code == 200
    assert 'wigglytuff' == response.json()['name']
    assert 'poketest' == response.json()['custom_name']
    assert 1 == response.json()['trainer_id']
