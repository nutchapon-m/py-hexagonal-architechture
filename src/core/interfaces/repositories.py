"""
This code section deals with creating an example of communication or data 
transmission between the database layer and the service layer. 
According to the concept of hexanal software architecture, 
the communication between the business logic part and the database part is clearly separated 
and should not be directly connected. But there should be a middleman
to help communicate between the two sides instead.
"""
from abc import ABC, abstractmethod
from contextlib import contextmanager
from typing import List, Dict, Any, Sequence
from sqlalchemy.orm import Session

class BaseRepository:
    def __init__(self, session: Session) -> None:
        self.session = session
        
    @contextmanager
    def _get_session(self):
        with self.session as db:
            try:
                yield db
            except:
                db.rollback()