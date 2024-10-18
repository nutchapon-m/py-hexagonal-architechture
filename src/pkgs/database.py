"""
this code section about instance database connection.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, DeclarativeBase

# By default we instance postgesql database connection.
DATABASE_URL = "postgresql://user:password@localhost:5432/dbname"

engine = create_engine(DATABASE_URL, echo=True)

session = Session(bind=engine)

class Base(DeclarativeBase):
    """
    Base abtract class instance for map dataclass with database schemas
    """
    pass