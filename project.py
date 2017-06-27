from flask import Flask, render_template, request, redirect, jsonify, url_for, flash, session as login_session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Animal, Toy
import random, string

app = Flask(__name__)

engine = create_engine('sqlite:///animal_toys.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html')


@app.route('/animals/JSON')
def animalsJSON():
    animals = session.query(Animal).all()
    return jsonify(animals=[animal.serialize for animal in animals])


@app.route('/animal/<int:animal_id>/toys/JSON')
def oneAnimalsToysJSON(animal_id):
    animal = session.query(Animal).filter_by(id=animal_id).one()
    toys = session.query(Toy).filter_by(animal_id=animal_id).all()
    return jsonify(Toys=[toy.serialize for toy in toys])


@app.route('/animal/<int:animal_id>/toys/<int:toy_id>/JSON')
def oneAnimalsOneToyJSON(animal_id, toy_id):
    oneToy = session.query(Toy).filter_by(id=toy_id).one()
    return jsonify(oneToy=oneToy.serialize)


@app.route('/')
@app.route('/animals')
def showAnimals():
    animals = session.query(Animal).all()
    #return 'This page will list all the animals.'
    return render_template('animals.html', animals=animals)


@app.route('/animal/new', methods=['GET', 'POST'])
def newAnimal():
    if request.method == 'POST':
        newAnimal = Animal(name=request.form['name'],
                           age=request.form['age'],
                           species=request.form['species'])
        session.add(newAnimal)
        session.commit()
        flash('New animal created!')
        return redirect(url_for('showAnimals'))
    else:
        return render_template('newAnimal.html')


@app.route('/animal/<int:animal_id>/edit', methods=['GET', 'POST'])
def editAnimal(animal_id):
    editedAnimal = session.query(Animal).filter_by(id=animal_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedAnimal.name = request.form['name']
        if request.form['age']:
            editedAnimal.age = request.form['age']
        if request.form['species']:
            editedAnimal.species = request.form['species']
        session.add(editedAnimal)
        session.commit()
        flash('Animal successfully edited!')
        return redirect(url_for('showAnimals'))
    else:
        return render_template('editAnimal.html', animal=editedAnimal)


@app.route('/animal/<int:animal_id>/delete', methods=['GET', 'POST'])
def deleteAnimal(animal_id):
    animalForRemoval = session.query(Animal).filter_by(id=animal_id).one()
    if request.method == 'POST':
        session.delete(animalForRemoval)
        session.commit()
        flash('Animal successfully deleted!')
        return redirect(url_for('showAnimals', animal_id=animal_id))
    else:
        return render_template('deleteAnimal.html', animal=animalForRemoval)


@app.route('/animal/<int:animal_id>')
@app.route('/animal/<int:animal_id>/toys')
def showToys(animal_id):
    animal = session.query(Animal).filter_by(id=animal_id).one()
    toys = session.query(Toy).filter_by(animal_id=animal_id).all()
    return render_template('toys.html', toys=toys, animal=animal)


@app.route('/animal/<int:animal_id>/toys/new', methods=['GET', 'POST'])
def newToy(animal_id):
    if request.method == 'POST':
        newToy = Toy(name=request.form['name'],
                     toy_type=request.form['toy_type'],
                     description=request.form['description'], animal_id=animal_id)
        session.add(newToy)
        session.commit()
        flash('New toy created!')
        return redirect(url_for('showToys', animal_id=animal_id))
    else:
        return render_template('newToy.html', animal_id=animal_id)


@app.route('/animal/<int:animal_id>/toys/<int:toy_id>/edit', methods=['GET', 'POST'])
def editToy(animal_id, toy_id):
    editedToy = session.query(Toy).filter_by(id=toy_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedToy.name = request.form['name']
        if request.form['toy_type']:
            editedToy.toy_type = request.form['toy_type']
        if request.form['description']:
            editedToy.description = request.form['description']
        session.add(editedToy)
        session.commit()
        flash('Toy successfully edited!')
        return redirect(url_for('showToys', animal_id=animal_id))
    else:
        return render_template('editToy.html', animal_id=animal_id, toy_id=toy_id, toy=editedToy)


@app.route('/animal/<int:animal_id>/toys/<int:toy_id>/delete', methods=['GET', 'POST'])
def deleteToy(animal_id, toy_id):
    toyForRemoval = session.query(Toy).filter_by(id=toy_id).one()
    if request.method == 'POST':
        session.delete(toyForRemoval)
        session.commit()
        flash('Toy successfully deleted!')
        return redirect(url_for('showToys', animal_id=animal_id))
    else:
        return render_template('deleteToy.html', toy=toyForRemoval)


if __name__ == '__main__':
    app.secret_key = 'secret_key_!@#'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
