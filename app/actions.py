from sqlalchemy.orm import Session
from . import models, schemas
from .utils.pokeapi import get_pokemon_name
from .utils.pokeapi import battle_pokemon


def get_trainer(database: Session, trainer_id: int):
    """
        Find a user by his id
    """
    return database.query(models.Trainer).filter(models.Trainer.id == trainer_id).first()


def get_trainer_by_name(database: Session, name: str):
    """
        Find a user by his name
    """
    return database.query(models.Trainer).filter(models.Trainer.name == name).all()


def get_trainers(database: Session, skip: int = 0, limit: int = 100):
    """
        Find all users
        Default limit is 100
    """
    return database.query(models.Trainer).offset(skip).limit(limit).all()


def create_trainer(database: Session, trainer: schemas.TrainerCreate):
    """
        Create a new trainer
    """
    db_trainer = models.Trainer(name=trainer.name, birthdate=trainer.birthdate)
    database.add(db_trainer)
    database.commit()
    database.refresh(db_trainer)
    return db_trainer


def add_trainer_pokemon(database: Session, pokemon: schemas.PokemonCreate, trainer_id: int):
    """
        Create a pokemon and link it to a trainer
    """
    db_item = models.Pokemon(
        **pokemon.dict(), name=get_pokemon_name(pokemon.api_id), trainer_id=trainer_id)
    database.add(db_item)
    database.commit()
    database.refresh(db_item)
    return db_item


def add_trainer_item(database: Session, item: schemas.ItemCreate, trainer_id: int):
    """
        Create an item and link it to a trainer
    """
    db_item = models.Item(**item.dict(), trainer_id=trainer_id)
    database.add(db_item)
    database.commit()
    database.refresh(db_item)
    return db_item


def get_items(database: Session, skip: int = 0, limit: int = 100):
    """
        Find all items
        Default limit is 100
    """
    return database.query(models.Item).offset(skip).limit(limit).all()


def get_pokemon(database: Session, pokemon_id: int):
    """
        Find a pokemon by his id
    """
    result =  database.query(models.Pokemon).filter(models.Pokemon.id == pokemon_id).first()
    return result

def get_pokemons(database: Session, skip: int = 0, limit: int = 100):
    """
        Find all pokemons
        Default limit is 100
    """
    return database.query(models.Pokemon).offset(skip).limit(limit).all()

def combat_pokemons(database: Session, pokemon_id_first: int, pokemon_id_second: int):
    """
        Find best pokemon between two
    """
    first_pokemon = database.query(models.Pokemon).filter(models.Pokemon.id == pokemon_id_first).first()
    second_pokemon = database.query(models.Pokemon).filter(models.Pokemon.id == pokemon_id_second).first()
    result = battle_pokemon(first_pokemon, second_pokemon)
    return result