from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Animal, Toy

engine = create_engine('sqlite:///animal_toys.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Toys for Riley the giraffe
giraffe1 = Animal(name = 'Riley', age = 22, species = 'Giraffe')

session.add(giraffe1)
session.commit()

toy1 = Toy(name = "Antlers", type = "Sensory", animal = giraffe1)

session.add(toy1)
session.commit()
