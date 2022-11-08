"""Module providingFunction printing python version."""
from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter,  Depends
# This is a placeholder for correct code for this message.
from ..utils.utils import get_db
from .. import actions, schemas


router = APIRouter()


@router.get("/", response_model=List[schemas.Item])
def get_items(skip: int = 0, limit: int = 100, database: Session = Depends(get_db)):
    """
        Return all items
        Default limit is 100
    """
    items = actions.get_items(database, skip=skip, limit=limit)
    return items
