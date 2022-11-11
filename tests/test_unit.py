from http import client
from urllib import response
from fastapi.testclient import TestClient
import pytest
from main import app
from random import randint
client = TestClient(app)


####################################
#           UNIT TESTS             #
####################################

# Test 1 
# Create new trainer and check if it has been created 
def test_trainer_created():
    trainer_name='Axel'
    trainer_id=1
    response = client.get(f"/trainers/{trainer_id}")
    assert response.status_code == 200
    assert response.json()['name'] == trainer_name

# Test 2
# Check the get trainers endpoint
def test_get_trainers():
    response = client.get("/trainers")
    assert response.status_code == 200
    assert len(response.json()) > 0

# Test 3
# Check the get items endpoint
def test_get_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert len(response.json()) > 0

# Test 4
def test_get_pokemon():
    response = client.get("/pokemons")
    assert response.status_code == 200
    assert len(response.json()) > 0

# Test 5
def test5():
    pass

# Test 6
def test6():
    pass

# Test 7
def test7():
    pass
