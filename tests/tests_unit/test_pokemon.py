import math
from fastapi.testclient import TestClient
from main import app
import pytest
from random import randint
client = TestClient(app)

def test_getPokemons():
    response = client.get("/pokemons")
    assert response.status_code == 200

