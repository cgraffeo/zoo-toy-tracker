from flask import Flask
app = Flask(__name__)

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from database_setup import Base, Animal, Toy
#
# engine = create_engine('sqlite:///animal_toys.db')
# Base.metadata.bind = engine
#
# DBSession = sessionmaker(bind=engine)
# session = DBSession

@app.route('/')
@app.route('/animals')
def showAnimals():
    #animals = session.query(Animal).all()
    return 'This page will list all the animals.'


@app.route('/animal/<int:animal_id>/')
@app.route('/animal/<int:animal_id>/toys/')
def showToys(animal_id):
    return 'This page will list the toys for a particular animal.'




if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8083)
