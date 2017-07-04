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

gorilla1_toy2 = Toy(name='Swings', toy_type='Environmental', description='Large swings for entertainment. Watch for Tino to make sure he does not wrap it around himself.', photo='https://2ecffd01e1ab3e9383f0-07db7b9624bbdf022e3b5395236d5cf8.ssl.cf4.rackcdn.com/Product-800x800/98745f7b-b53d-4951-b632-2c63e70b8489.jpg', animal=gorilla1, user_id=1)

session.add(gorilla1_toy2)
session.commit()

gorilla1_toy3 = Toy(name='Tug-o-war', toy_type='Behavioral/Social', description='A very sturdy rope for use between animal/keeper or animal/animal. Be careful with this one!', photo='https://www.globalbodyweighttraining.com/wp-content/uploads/GBT-Manila-Rope-Knot.jpg', animal=gorilla1, user_id=1)

session.add(gorilla1_toy3)
session.commit()
# End toys for Tino

# Toys for Zuri the elephant
elephant1 = Animal(name='Zuri', age=10, species='Elephant', photo='https://static1.squarespace.com/static/5304f39be4b0c1e749b456be/t/58cc06d96a49637cb9ed84a6/1489766903764/', user_id=1)

session.add(elephant1)
session.commit()

elephant1_toy_1 = Toy(name='Bubbles', toy_type='Sensory', description='The keeper can blow NON-TOXIC bubbles into the elephant exhibit. The elephants like to chase them around.', photo='https://assets.bwbx.io/images/users/iqjWHBFdfxIU/iz9tFMUcP6rI/v1/1200x-1.jpg', animal=elephant1, user_id=1)

session.add(elephant1_toy_1)
session.commit()
# End toys for Zuri

# Toys for Kazek the tiger
tiger1 = Animal(name='Kazek', age=13, species='Tiger', photo='http://www.wildaid.org/sites/default/files/photos/iStock_000008484745Large%20%20tiger%20-%20bengal.jpg', user_id=1)

session.add(tiger1)
session.commit()

tiger1_toy1 = Toy(name='Disco Ball', toy_type='Sensory', description='The little lights off this disco ball are like using a laser on a house cat; The tigers love to chase them around.', animal=tiger1, user_id=1)

session.add(tiger1_toy1)
session.commit()
# End toys for Kazek

# Toys for Kwan the crocodile
crocodile1 = Animal(name='Kwan', age=6, species='Crocodile', photo='https://s-media-cache-ak0.pinimg.com/736x/8d/92/2e/8d922e642ce725024ec741bff8bc7175--darwin-australia-saltwater-crocodile.jpg', user_id=1)

session.add(crocodile1)
session.commit()

crocodile1_toy1 = Toy(name='Branches', toy_type='Environmental', description='The crocs love to hide in the branches. Maybe they like the privacy?', animal=crocodile1, user_id=1)

session.add(crocodile1_toy1)
session.commit()
# End toys for Kwan

# Toys for Sam the eagle
eagle1 = Animal(name='Sam', age=4, species='Bald Eagle', photo='https://identify.whatbird.com/img/4/48397/image.aspx?x=322', user_id=1)

session.add(eagle1)
session.commit()

eagle1_toy1 = Toy(name='Straw Pile', toy_type='Environmental', description='The eagles love to carry this into their favorite corner of the exhibit. Seems like they try to build a nest with it.', animal=eagle1, user_id=1)

session.add(eagle1_toy1)
session.commit()
# End toys for Sam
