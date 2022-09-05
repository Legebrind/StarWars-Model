import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

PeopleFavorite = Table("PeopleFavorite", Base.metadata,  
    Column("userId",Integer, ForeignKey("user.id"),primary_key=True),
    Column("peopleId",Integer, ForeignKey("people.id"),primary_key=True))

PlanetFavorite = Table("PlanetFavorite", Base.metadata,
    Column("userId",Integer, ForeignKey("user.id"),primary_key=True),
    Column("planetId",Integer, ForeignKey("planet.id"),primary_key=True))
    


class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    gender = Column(String(100), unique=False, nullable=False)
    hair_color = Column(String(100), unique=False, nullable=False)
    eye_color = Column(String(100), unique=False, nullable=False)

    def __repr__(self):
        return f'<People id ={self.id}, name= {self.name}, gender={self.gender},hair_color = {self.hair_color}, eye_color = {self.eye_color}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color            
        }

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    population = Column(String(120), unique=False, nullable=False)
    terrain = Column(String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Planet id={self.id}, name={self.name}, population ={self.population}, terrain={self.terrain}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "terrain": self.terrain            
        }

class User(Base):
    __tablename__="user"
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), unique=False, nullable=False)
    """ is_active = Column(Boolean(), unique=False, nullable=False) """
    people_favorite = relationship('People', secondary=PeopleFavorite, lazy='subquery',
        backref="favorite people")
    planet_favorite = relationship('Planet', secondary=PlanetFavorite, lazy='subquery',
        backref="favorite planets")

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active" : self.is_active
            # do not serialize the password, its a security breach
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')