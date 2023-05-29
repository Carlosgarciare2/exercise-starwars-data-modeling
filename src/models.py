import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    climate = Column(String(250))
    diameter = Column(String(250))
    gravity = Column(String(250))
    orbital_period = Column(String(250))
    population = Column(String(250))
    terrain = Column(String(250))
    
class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    eye_color = Column(String(250))
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    gender = Column(String(250))
    height = Column(String(250))
    birth_year = Column(String(250))

class Favorites(Base):
    __tablename__= 'favorites'
    id = Column(Integer, primary_key=True)
    planet_id: Column(Integer, ForeignKey('planet.id'))
    character_id: Column(Integer, ForeignKey('character.id'))

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(130), nullable=False)
    email = Column(String(130), nullable=False)
    password = Column(String(130), nullable=False)
    favorites_id = Column (Integer, ForeignKey('favorites.id'))



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
