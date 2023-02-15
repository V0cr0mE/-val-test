from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter,  Depends
from app import actions, schemas
from app.utils.utils import get_db
from app.utils.pokeapi import get_pokemon_name
from app.utils.pokeapi import get_pokemon_stats
from random import randint
from app.utils.pokeapi import battle_pokemon

router = APIRouter()


@router.get("/", response_model=List[schemas.Pokemon])
def get_pokemons(skip: int = 0, limit: int = 100, database: Session = Depends(get_db)):
    """
        Return all pokemons
        Default limit is 100
    """
    pokemons = actions.get_pokemons(database, skip=skip, limit=limit)
    return pokemons

@router.get('/get_three_random_pokemons', response_model=List)
def get_three_random_pokemons(database: Session = Depends(get_db)):
    """
        Return three random pokemons names + stats
    """
    liste = [randint(1, 1008) for i in range(3)]
    return [{'name': get_pokemon_name(i), 'stats': get_pokemon_stats(i)} for i in liste]


@router.get("/fight/{id_pokemon_1}/{id_pokemon_2}")
def get_pokemons_fight(
    id_pokemon_1: int, id_pokemon_2: int, database: Session = Depends(get_db)
):
    return battle_pokemon(id_pokemon_1, id_pokemon_2)
