from sqlalchemy.orm import Session
from fastapi import APIRouter,  Depends
from app.utils.utils import get_db
from app import actions, schemas


router = APIRouter()

@router.get("/{id_first_pokemon}/{id_second_pokemon}")
def get_combat_result(
    id_first_pokemon: int, id_second_pokemon: int, database: Session = Depends(get_db)
):
    """
        Return winner between two trainer pokemons
    """
    return actions.combat_pokemons(database, pokemon_id_first=id_first_pokemon,pokemon_id_second=id_second_pokemon)
