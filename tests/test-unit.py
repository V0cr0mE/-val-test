import unittest
from app.utils.pokeapi import battle_pokemon

class TestBattlePokemon(unittest.TestCase):

    def test_battle_pokemon(self):
        # Define test inputs
        first_api_id = 257
        second_api_id = 124

        # Test battle_pokemon function
        result = battle_pokemon(first_api_id, second_api_id)

        # Assertions
        self.assertIn('draw', result['winner'])
