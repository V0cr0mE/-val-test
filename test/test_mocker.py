from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Combat pokemon
def test_pokemon_battle(mocker):
    """
        Resultat de la comparaison de stats
    """
    mocker.patch("app.utils.pokeapi.battle_compare_stats", return_value=1)
    response = client.get("/pokemons/battle/2/6")
    assert response.status_code == 200
    assert response.json() == 2

# Combat pokemon
def test_pokemon_battle_draw(mocker):
    """
        Resultat de la comparaison de stats si egalite
    """
    mocker.patch("app.utils.pokeapi.battle_compare_stats", return_value=0)
    response = client.get("/pokemons/battle/2/6")
    assert response.status_code == 200
    assert response.json() == {'winner': 'draw'}

    # Create Trainer
def test_create_trainer(mocker):
    """
        Creation d'un trainer
    """
    mocker.patch("app.actions.create_trainer", return_value={"name": "balou", "birthdate": "2012-11-07", "id": 8, "inventory": [], "pokemons": []})
    response = client.post("/trainers/", json={"name": "balou", "birthdate": "2012-11-07"})
    assert response.status_code == 200
    assert response.json() == {"name": "balou", "birthdate": "2012-11-07", "id": 8, "inventory": [], "pokemons": []}
