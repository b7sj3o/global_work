from typing import Tuple
import os
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session as SessionType


class classproperty:
    def __init__(self, method):
        self.method = method
    def __get__(self, obj, cls=None):
        if cls is None:
            cls = type(obj)
        return self.method(cls)
    
    
class Base(DeclarativeBase):
    """
    Base class for every SQLAlchemy model that
    automatically generates table name (SQLAlchemy model name + "s")

    e.g. model "User" -> __tablename__="users"
    """

    @classproperty
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"
   
    
engine = create_engine(f"sqlite:///backend/db.sqlite3", echo=True)
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)