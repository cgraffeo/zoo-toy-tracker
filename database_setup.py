import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Animal(Base):
    __tablename__ = 'animal'

    id = Column(Integer, primary_key = True)
    name = Column(String(10), nullable = False)
    age = Column(Integer)
    species = Column(String(50), nullable = False)


class Toy(Base):
    __tablename__ = 'toy'

    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    animal_id = Column(Integer, ForeignKey('animal.id'))
    type = Column(String(10))
    animal = relationship(Animal)


engine = create_engine('sqlite:///animal_toys.db')
Base.metadata.create_all(engine)
