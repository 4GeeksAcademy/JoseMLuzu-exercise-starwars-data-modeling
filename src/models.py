import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(50))
    password = Column(String(50))  

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    population = Column(Integer)
    terrain = Column(String(50))
    climate = Column(String(50))

class Favorite_Planet(Base):
    __tablename__ = "favorite_planet"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user_id_relationship = relationship(User)
    planet_id = Column(Integer, ForeignKey("planets.id"), nullable=False)  
    planet_id_relationship = relationship(Planets)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    last_name = Column(String(50))
    height = Column(Integer)
    mass = Column(Integer)

class Favorite_Character(Base):
    __tablename__ = "favorite_character"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user_id_relationship = relationship(User)
    character_id = Column(Integer, ForeignKey("characters.id"), nullable=False)  
    character_id_relationship = relationship(Characters)

class Starships(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    manufacturer = Column(String(50))
    mass = Column(String(50))  

class Favorite_Starship(Base):
    __tablename__ = "favorite_starship"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user_id_relationship = relationship(User)
    starship_id = Column(Integer, ForeignKey("starship.id"), nullable=False)  
    starship_id_relationship = relationship(Starships)

    def to_dict(self):
        return {}

## Dibuja desde la base de datos SQLAlchemy
render_er(Base, 'diagram.png')
