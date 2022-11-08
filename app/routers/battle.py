from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter,  Depends, HTTPException
from ..utils.utils import get_db
from ..utils import pokeapi
from .. import actions, schemas
router = APIRouter()


@router.post("/", response_model=schemas.BattleResult)
def battle(pokemon_right: schemas.Pokemon, pokemon_left: schemas.Pokemon):
    """
        Do battle between 2 trainer
    """
    pokemon_victorieux = pokeapi.battle_pokemon(
        pokemon_right.api_id, pokemon_left.api_id)
    print(pokemon_victorieux)
    if pokemon_victorieux['winner'] == "right":
        pokemon_victorieux['winner'] = str(pokemon_right.id)
        return pokemon_victorieux
    elif pokemon_victorieux['winner'] == "left":
        pokemon_victorieux['winner'] = str(pokemon_left.id)
        return pokemon_victorieux
    else:
        return pokemon_victorieux
