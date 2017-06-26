from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Animal, Toy

app = Flask(__name__)

engine = create_engine('sqlite:///animal_toys.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/animals')
def showAnimals():
    animals = session.query(Animal).all()
    #return 'This page will list all the animals.'
    return render_template('animals.html', animals=animals)


@app.route('/animal/new', methods=['GET', 'POST'])
def newAnimal():
    return 'This page will be for making a new animal'
    # if request.method == 'POST':
    #     newAnimal = Animal(name=request.form['name'])
    #     session.add(newAnimal)
    #     session.commit()
    #     return redirect(url_for('showAnimals'))
    # else:
    #     return render_template('newAnimal.html')


@app.route('/animal/<int:animal_id>/edit', methods=['GET', 'POST'])
def editAnimal(animal_id):
    return 'This page will be for editing this animal'


@app.route('/animal/<int:animal_id>/delete', methods=['GET', 'POST'])
def deleteAnimal(animal_id):
    return 'This page will be for deleting this animal'


@app.route('/animal/<int:animal_id>')
@app.route('/animal/<int:animal_id>/toys')
def showToys(animal_id):
    animal = session.query(Animal).filter_by(id=animal_id).one()
    toys = session.query(Toy).filter_by(animal_id=animal_id).all()
    #return 'This page will list the toys for a particular animal.'
    return render_template('toys.html', toys=toys, animal=animal)


@app.route('/animal/<int:animal_id>/toys/new', methods=['GET', 'POST'])
def newToy(animal_id):
    return 'This page will be for making a new toy for this animal'


@app.route('/animal/<int:animal_id>/toys/<int:toy_id>/edit', methods=['GET', 'POST'])
def editToy(animal_id, toy_id):
    return 'This page will be for editing this toy for this animal'


@app.route('/animal/<int:animal_id>/toys/<int:toy_id>/delete', methods=['GET', 'POST'])
def deleteToy(animal_id, toy_id):
    return 'This page will be for deleting this toy for this animal'


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
