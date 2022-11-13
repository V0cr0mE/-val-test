from fastapi.testclient import TestClient
from main import app
import json

client = TestClient(app)


draw_data = open('../resources/draw.json')
response_draw_data = {"winner": "draw"}

poke1_data = open('../resources/poke1_win.json')
response_win1_data = {"winner": "1"}

poke2_data = open('../resources/poke2_win.json')
response_win2_data = {"winner": "2"}

def test_battle_draw_should_respond_with_200_and_draw():
    #Given/When
    response = client.post(
            "/battle/1/2",
            headers={'accept': 'application/json', 'Content-Type': 'application/json'},
            draw_data= json.dumps(draw_data)
        )
    
    #Then
    assert response.status_code == 200
    assert response.json() == response_draw_data

def test_battle_win_poke1_should_respond_with_200_and_win_poke1():
    #Given/When
    response = client.post(
            "/battle/1/2",
            headers={'accept': 'application/json', 'Content-Type': 'application/json'},
            draw_data= json.dumps(draw_data)
        )
    
    #Then
    assert response.status_code == 200
    assert response.json() == response_win1_data

def test_battle_win_poke2_should_respond_with_200_and_win_poke2():
    #Given/When
    response = client.post(
            "/battle/1/2",
            headers={'accept': 'application/json', 'Content-Type': 'application/json'},
            draw_data= json.dumps(draw_data)
        )
    
    #Then
    assert response.status_code == 200
    assert response.json() == response_win2_data