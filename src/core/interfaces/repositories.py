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
    
class UserRepository(ABC):
    @abstractmethod
    async def get_all(self):
        raise NotImplementedError()
    
class UserRepositoriesDB(UserRepository):
    def __init__(self, session: Session) -> None:
        self.base = BaseRepository(session)

    async def get_all(self):
        with self.base._get_session() as conn:
            conn
        return await super().get_all()
    
    async def get_by_id(self, id: int):
        return None

def new_user_repo(session: Session) -> UserRepository:
    return UserRepositoriesDB(session)

use = new_user_repo(session=Session())

use