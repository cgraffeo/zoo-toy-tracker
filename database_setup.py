import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    picture = Column(String(250))


class Animal(Base):
    __tablename__ = 'animal'

    id = Column(Integer, primary_key = True)
    name = Column(String(30), nullable = False)
    age = Column(Integer)
    species = Column(String(50), nullable = False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'species': self.species
        }


class Toy(Base):
    __tablename__ = 'toy'

    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    animal_id = Column(Integer, ForeignKey('animal.id'))
    toy_type = Column(String(10))
    description = Column(String(160))
    animal = relationship(Animal)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'animal_id': self.animal_id,
            'toy_type': self.toy_type,
            'description': self.description
        }


engine = create_engine('sqlite:///animal_toys.db')
Base.metadata.create_all(engine)
