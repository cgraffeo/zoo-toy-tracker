from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Animal, Toy

engine = create_engine('sqlite:///animal_toys.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Toys for Riley the giraffe
giraffe1 = Animal(name = 'Riley', age = 22, species = 'Giraffe', user_id=1)

session.add(giraffe1)
session.commit()

giraffe1_toy1 = Toy(name = 'Antlers', toy_type = 'Sensory', description = 'Antlers from a deer that provide sensory stimulation for the animal.', animal = giraffe1, user_id=1)

session.add(giraffe1_toy1)
session.commit()

giraffe1_toy2 = Toy(name = 'Barrel Feeder', toy_type = 'Foods and Feeding', description = 'Just like it sounds. Food placed in a barrel with enough openings for access, but cleverly placed for a stimulating challenge.', animal = giraffe1, user_id=1)

session.add(giraffe1_toy2)
session.commit()

giraffe1_toy3 = Toy(name = 'Pinecones', toy_type = 'Manipulative', description = 'Pine cones used for an interactive toy for removing parts.', animal = giraffe1, user_id=1)

session.add(giraffe1_toy3)
session.commit()

# End toys for Riley

# Toys for Tino the gorilla
gorilla1 = Animal(name = 'Tino', age = 15, species = 'Gorilla', user_id=1)

session.add(gorilla1)
session.commit()

gorilla1_toy1 = Toy(name = 'TV/Videos', toy_type = 'Sensory', description = 'Pretty obvious what this is. Should only be used for 30 minutes or less a day.', animal = gorilla1, user_id=1)

session.add(gorilla1_toy1)
session.commit()

gorilla1_toy2 = Toy(name = 'Swings', toy_type = 'Environment', description = 'Large swings for entertainment. Watch for Tino to make sure he does not wrap it around himself.', animal = gorilla1, user_id=1)

session.add(gorilla1_toy2)
session.commit()

gorilla1_toy3 = Toy(name = 'Tug-o-war', toy_type = 'Behavioral/Social', description = 'A very sturdy rope for use between animal/keeper or animal/animal. Be careful with this one!', animal = gorilla1, user_id=1)

session.add(gorilla1_toy3)
session.commit()
