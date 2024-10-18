"""
This section of code is about creating a model for mapping to tables schemas in the database. 
This template uses an ORM framework like sqlalchemy, which is widely used in web development 
using the Python language.
"""
from sqlalchemy import (
    String, 
    Integer, 
    Float, 
    DateTime, 
    Date, 
    ForeignKey
)
from sqlalchemy.orm import (
    Mapped, 
    mapped_column, 
    relationship
)