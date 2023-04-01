import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Characters(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    height = Column(String(250))
    mass = Column(String(250))
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))
  
    birth_planet = Column(Integer(), ForeignKey("planets.id") )
    card_id = Column(Integer, ForeignKey("cards.id"))


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    gravity = Column(Integer())
    diameter = Column(Integer())
    population = Column(Integer())
    rotation_period = Column(Integer())
    orbital_period = Column(Integer())
    climate = Column(String(250))
    terrain = Column(String(250))
    water_on_surface = Column(String(250))

    card_id = Column(Integer, ForeignKey("cards.id"))



class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(250), nullable=False)
    full_name = Column(String(250))
    password = Column(Integer)
    email = Column(String(250))



class Favourites(Base):
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    card_id = Column(Integer, ForeignKey("cards.id"))

    
class Cards(Base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True)






# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
