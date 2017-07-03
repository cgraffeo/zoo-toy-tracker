from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Animal, Toy

engine = create_engine('sqlite:///animal_toys.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Toys for Riley the giraffe
giraffe1 = Animal(name='Riley', age=22, species='Giraffe', photo='http://animalinyou.com/images/animals/giraffe/giraffe-2.jpg', user_id=1)

session.add(giraffe1)
session.commit()

giraffe1_toy1 = Toy(name='Antlers', toy_type='Sensory', description='Antlers from a deer that provide sensory stimulation for the animal.', photo='http://cdn0.wideopenspaces.com/wp-content/uploads/2014/01/featured-antlers.jpg', animal=giraffe1, user_id=1)

session.add(giraffe1_toy1)
session.commit()

giraffe1_toy2 = Toy(name='Barrel Feeder', toy_type='Foods and Feeding', description='Just like it sounds. Food placed in a barrel with enough openings for access, but cleverly placed for a stimulating challenge.', photo='https://images-na.ssl-images-amazon.com/images/I/41Qj8Bh185L._SY355_.jpg', animal=giraffe1, user_id=1)

session.add(giraffe1_toy2)
session.commit()

giraffe1_toy3 = Toy(name='Pinecones', toy_type='Manipulative', description='Pine cones used for an interactive toy for removing parts.', photo='http://www.timespub.tc/wp-content/uploads/2012/01/Pine-cones-1.jpg', animal=giraffe1, user_id=1)

session.add(giraffe1_toy3)
session.commit()

# End toys for Riley

# Toys for Tino the gorilla
gorilla1 = Animal(name='Tino', age=15, species='Gorilla', photo='http://animals.sandiegozoo.org/sites/default/files/2016-09/Gorilla_ZN.jpg', user_id=1)

session.add(gorilla1)
session.commit()

gorilla1_toy1 = Toy(name='TV/Videos', toy_type='Sensory', description='Pretty obvious what this is. Should only be used for 30 minutes or less a day.', photo='http://sugikingdom.com/wp-content/uploads/2016/12/2017-TV-GUide.jpg', animal=gorilla1, user_id=1)

session.add(gorilla1_toy1)
session.commit()

gorilla1_toy2 = Toy(name='Swings', toy_type='Environment', description='Large swings for entertainment. Watch for Tino to make sure he does not wrap it around himself.', photo='https://2ecffd01e1ab3e9383f0-07db7b9624bbdf022e3b5395236d5cf8.ssl.cf4.rackcdn.com/Product-800x800/98745f7b-b53d-4951-b632-2c63e70b8489.jpg', animal=gorilla1, user_id=1)

session.add(gorilla1_toy2)
session.commit()

gorilla1_toy3 = Toy(name='Tug-o-war', toy_type='Behavioral/Social', description='A very sturdy rope for use between animal/keeper or animal/animal. Be careful with this one!', photo='https://www.globalbodyweighttraining.com/wp-content/uploads/GBT-Manila-Rope-Knot.jpg', animal=gorilla1, user_id=1)

session.add(gorilla1_toy3)
session.commit()
