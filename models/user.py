#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
import os


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = "users"
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        email = Column(String(128), unique=True, nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), unique=True, nullable=True)
        last_name = Column(String(128), unique=True, nullable=True)
        places = relationship("Place", backref="user",
                              cascade="all, delete, delete-orphan")

        # reviews = relationship("Review", backref="user",
        #                        cascade="all, delete, delete-orphan")
    else:
        id = ""
        email = ""
        password = ""
        first_name = ""
        last_name = ""
        places = ""
        reviews = ""
