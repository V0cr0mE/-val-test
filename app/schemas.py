"""
Shemas
"""

from datetime import date
from typing import  List, Optional, Union
from pydantic import BaseModel

#
#  ITEM
#
class ItemBase(BaseModel):
    """
        Base Items
    """
    name: str
    description: Union[str, None] = None


class ItemCreate(ItemBase):
    """
        Create item
    """

class Item(ItemBase):
    """
        item
    """
    id: int
    trainer_id: int

    class Config:
        """
        Config
        """
        orm_mode = True

#
#  POKEMON
#
class PokemonBase(BaseModel):
    """
        Pokemon base
    """
    api_id: int
    custom_name: Optional[str] = None

class PokemonCreate(PokemonBase):
    """
        pokemonCreate
    """

class Pokemon(PokemonBase):
    """
        pokemon
    """
    id: int
    name: str
    trainer_id: int

    class Config:
        """
            Config
        """
        orm_mode = True


#
#  TRAINER
#
class TrainerBase(BaseModel):
    """
        Trainer Base
    """
    name: str
    birthdate: date



class TrainerCreate(TrainerBase):
    """
        Trainer Create
    """

class Trainer(TrainerBase):
    """
        Trainer
    """
    id: int
    inventory: List[Item] = []
    pokemons: List[Pokemon] = []

    class Config:
        """
            Config
        """
        orm_mode = True
