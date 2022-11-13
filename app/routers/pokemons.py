"""
pokemons db
"""

from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import actions, schemas
from app.utils import pokeapi
from app.utils.utils import get_db

router = APIRouter()


@router.get("/", response_model=List[schemas.Pokemon])
def get_pokemons(skip: int = 0, limit: int = 100, database: Session = Depends(get_db)):
    """
        Return all pokemons
        Default limit is 100
    """
    pokemons = actions.get_pokemons(database, skip=skip, limit=limit)
    return pokemons

@router.get("/battle/{api_id}/{api_id2}")

def battle_pokemon(api_id,api_id2):
    """
        Return pokemon win
    """
    return pokeapi.battle_pokemon(api_id,api_id2)
    