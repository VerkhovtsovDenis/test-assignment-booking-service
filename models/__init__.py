from .Base import Base
from .Table import Table
from .Reservation import Reservation
from sqlalchemy import create_engine
from config import get_db_url

__all__ = (
    "Base"
    "Table"
    "Reservation"
)

db = create_engine(get_db_url())
