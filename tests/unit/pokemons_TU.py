from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

data = open('../resources/pokemon.json')

def test_pokemons(mocker):
    #Given
    data = open('../resources/pokemon.json')

    #When
    mocker.patch(
    "app.actions.get_pokemons",
    return_value= data
    )
    response = client.get("pokemons/?skip=0&limit=100")

    #Then
    assert response.status_code == 200
    assert response.json() == data
