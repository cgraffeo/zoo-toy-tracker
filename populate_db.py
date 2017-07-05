from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Animal, Toy

engine = create_engine('sqlite:///animal_toys.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Toys for Riley the giraffe
giraffe1 = Animal(name='Riley', age=22, species='Giraffe',
    photo='''
    https://www.gannett-cdn.com/-mm-/23a4d1bc400338a4d357213197131161c2b0c9ce/c=119-0-2001-1415&r=x404&c=534x401/local/-/media/2017/03/02/USATODAY/USATODAY/636240538720039138-GettyImages-509934328.jpg
    ''', user_id=1)

session.add(giraffe1)
session.commit()

giraffe1_toy1 = Toy(name='Antlers', toy_type='Sensory',
    description='''
    Antlers from a deer that provide sensory stimulation for the animal.''',
    photo='''
    http://img-aws.ehowcdn.com/300x200/cpi.studiod.com/www_ehow_com/photos.demandstudios.com/getty/article/235/128/466280485_XS.jpg
    ''', animal=giraffe1, user_id=1)

session.add(giraffe1_toy1)
session.commit()

giraffe1_toy2 = Toy(name='Barrel Feeder', toy_type='Foods and Feeding',
    description='''
    Just like it sounds. Food placed in a barrel with enough openings for
    access.''',
    photo='''
    https://images-na.ssl-images-amazon.com/images/I/41Qj8Bh185L._SY355_.jpg
    ''', animal=giraffe1, user_id=1)

session.add(giraffe1_toy2)
session.commit()

giraffe1_toy3 = Toy(name='Pinecones', toy_type='Manipulative',
    description='''
    Pine cones used for an interactive toy for removing parts.''',
    photo='http://www.winterwoods.com/art/cones/cone-sand.gif',
    animal=giraffe1, user_id=1)

session.add(giraffe1_toy3)
session.commit()
# End toys for Riley

# Toys for Tino the gorilla
gorilla1 = Animal(name='Tino', age=15, species='Gorilla',
    photo='http://pin.primate.wisc.edu/fs/sheets/images/235med.jpg', user_id=1)

session.add(gorilla1)
session.commit()

gorilla1_toy1 = Toy(name='TV/Videos', toy_type='Sensory',
    description='''
    Pretty obvious what this is. Should only be used for 30 minutes or less
    a day.''',
    photo='''
    http://az616578.vo.msecnd.net/files/2016/05/14/635988030950093450571401770_tv_bars.jpg
    ''', animal=gorilla1, user_id=1)

session.add(gorilla1_toy1)
session.commit()

gorilla1_toy2 = Toy(name='Swings', toy_type='Environmental',
    description='''
    Large swings for entertainment. Watch for Tino to make sure he does not
    wrap it around himself.''',
    photo='''
    https://2ecffd01e1ab3e9383f0-07db7b9624bbdf022e3b5395236d5cf8.ssl.cf4.rackcdn.com/Product-800x800/98745f7b-b53d-4951-b632-2c63e70b8489.jpg
    ''', animal=gorilla1, user_id=1)

session.add(gorilla1_toy2)
session.commit()

gorilla1_toy3 = Toy(name='Tug-o-war', toy_type='Behavioral/Social',
    description='''
    A very sturdy rope for use between animal/keeper or animal/animal.
    Be careful with this one!''',
    photo='https://i.stack.imgur.com/MMQggm.jpg', animal=gorilla1, user_id=1)

session.add(gorilla1_toy3)
session.commit()
# End toys for Tino

# Toys for Zuri the elephant
elephant1 = Animal(name='Zuri', age=10, species='Elephant',
    photo='''
    https://elephants-media.s3.amazonaws.com/App/Models/Elephant/images/000/000/004/thumbnail/Photo%20Of%20Flora%20At%20The%20Elephant%20Sanctuary%20In%20Tennessee.jpg
    ''', user_id=1)

session.add(elephant1)
session.commit()

elephant1_toy_1 = Toy(name='Bubbles', toy_type='Sensory',
    description='''
    The keeper can blow NON-TOXIC bubbles into the elephant exhibit.
    The elephants like to chase them around.''',
    photo='http://3dprint.com/wp-content/uploads/2015/07/bubble4.png',
    animal=elephant1, user_id=1)

session.add(elephant1_toy_1)
session.commit()
# End toys for Zuri

# Toys for Kazek the tiger
tiger1 = Animal(name='Kazek', age=13, species='Tiger',
    photo='''
    https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Bengal_Tiger.png/220px-Bengal_Tiger.png
    ''', user_id=1)

session.add(tiger1)
session.commit()

tiger1_toy1 = Toy(name='Disco Ball', toy_type='Sensory',
    description='''
    The little lights off this disco ball are like using a laser on a
    house cat; The tigers love to chase them around.''',
    photo='https://upload.wikimedia.org/wikipedia/commons/2/29/Disco_ball4.jpg',
    animal=tiger1, user_id=1)

session.add(tiger1_toy1)
session.commit()
# End toys for Kazek

# Toys for Kwan the crocodile
crocodile1 = Animal(name='Kwan', age=6, species='Crocodile',
    photo='''
    https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Nile_crocodile_head.jpg/260px-Nile_crocodile_head.jpg
    ''', user_id=1)

session.add(crocodile1)
session.commit()

crocodile1_toy1 = Toy(name='Branches', toy_type='Environmental',
    description='''The crocs love to hide in the branches.
    Maybe they like the privacy?''',
    photo='''
    http://pre04.deviantart.net/bc62/th/pre/i/2015/138/2/2/old_branch_png___by_welshdragonstocknart-d8tt7rf.png
    ''', animal=crocodile1, user_id=1)

session.add(crocodile1_toy1)
session.commit()
# End toys for Kwan

# Toys for Sam the eagle
eagle1 = Animal(name='Sam', age=4, species='Bald Eagle',
    photo='''
    http://naturemappingfoundation.org/natmap/photos/birds/bald_eagle_02tk.jpg
    ''', user_id=1)

session.add(eagle1)
session.commit()

eagle1_toy1 = Toy(name='Straw Pile', toy_type='Environmental',
    description='''The eagles love to carry this into their favorite corner
    of the exhibit. Seems like they try to build a nest with it.''',
    photo='''
    http://media.istockphoto.com/photos/straw-pile-on-blue-picture-id184292466?k=6&m=184292466&s=612x612&w=0&h=tQL272NaWHFSK-KGQo7lHBv7-us7UZ2zQEqY7xRYNuo=
    ''', animal=eagle1, user_id=1)

session.add(eagle1_toy1)
session.commit()
# End toys for Sam
