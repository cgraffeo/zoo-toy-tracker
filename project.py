import random
import string
import os
import json
import requests
import httplib2
from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask import flash, make_response, session as login_session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from oauth2client.client import flow_from_clientsecrets, FlowExchangeError
from database_setup import Base, Animal, Toy, User


app = Flask(__name__)


CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Zoo Toy Tracker"


engine = create_engine('sqlite:///animal_toys.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def login_required():
    if 'username' not in login_session:
        return redirect('/login')


@app.route('/')
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in range(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])

    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Get app's google credentials(client_id and client_secret) and google
    # plus id, and check if they're empty
    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(
            json.dumps('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    # ADD PROVIDER TO LOGIN SESSION
    login_session['provider'] = 'google'

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(data['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ''' " style = "width: 300px; height: 300px;border-radius:
    150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '''
    flash("You are now logged in as %s" % login_session['username'])
    print("DONE!")
    return output


# User Helper Functions
def createUser(login_session):
    newUser = User(name=login_session['username'],
                   email=login_session['email'],
                   picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


# DISCONNECT - Revoke a current user's token and reset their login_session
@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    access_token = login_session['access_token']
    if access_token is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = ('https://accounts.google.com/o/oauth2/revoke?token=%s'
            % login_session['access_token'])
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']

        response = make_response(json.dumps('Successfully disconnected'), 200)
        response.headers['Content-Type'] = 'application/json'
        return redirect(url_for('showAnimals'))
    else:
        response = make_response(
            json.dumps('Failed to revoke token for given user.'), 400)
        response.headers['Content-Type'] = 'application/json'
        return response


# JSON API endpoints
@app.route('/animals/JSON/')
def animalsJSON():
    animals = session.query(Animal).all()
    return jsonify(animals=[animal.serialize for animal in animals])


@app.route('/animal/<int:animal_id>/toys/JSON/')
def oneAnimalsToysJSON(animal_id):
    animal = session.query(Animal).filter_by(id=animal_id).one()
    toys = session.query(Toy).filter_by(animal_id=animal_id).all()
    return jsonify(Toys=[toy.serialize for toy in toys])


@app.route('/animal/<int:animal_id>/toys/<int:toy_id>/JSON/')
def oneAnimalsOneToyJSON(animal_id, toy_id):
    oneToy = session.query(Toy).filter_by(id=toy_id).one()
    return jsonify(oneToy=oneToy.serialize)
# End JSON routes


@app.route('/animals/')
def showAnimals():
    animals = session.query(Animal).all()
    if 'username' not in login_session:
        return render_template('publicAnimals.html', animals=animals)
    else:
        return render_template('animals.html', animals=animals)


@app.route('/animal/new/', methods=['GET', 'POST'])
def newAnimal():
    login_required()
    if request.method == 'POST':
        newAnimal = Animal(name=request.form['name'],
                           age=request.form['age'],
                           species=request.form['species'],
                           photo=request.form['photo'],
                           user_id=login_session['user_id'])
        session.add(newAnimal)
        session.commit()
        flash('%s successfully created!' % newAnimal.name)
        return redirect(url_for('showAnimals'))
    else:
        return render_template('newAnimal.html')


@app.route('/animal/<int:animal_id>/edit/', methods=['GET', 'POST'])
def editAnimal(animal_id):
    login_required()
    editedAnimal = session.query(Animal).filter_by(id=animal_id).one()
    if editedAnimal.user_id != login_session['user_id']:
        flash('You are not authorized to edit this animal.'
              'Please create your own animal in order to add, edit or remove.')
        return redirect(url_for('showAnimals'))
    if request.method == 'POST':
        if request.form['name']:
            editedAnimal.name = request.form['name']
        if request.form['age']:
            editedAnimal.age = request.form['age']
        if request.form['species']:
            editedAnimal.species = request.form['species']
        if request.form['photo']:
            editedAnimal.photo = request.form['photo']
        session.add(editedAnimal)
        session.commit()
        flash('%s successfully edited!' % editedAnimal.name)
        return redirect(url_for('showAnimals'))
    else:
        return render_template('editAnimal.html', animal=editedAnimal)


@app.route('/animal/<int:animal_id>/delete/', methods=['GET', 'POST'])
def deleteAnimal(animal_id):
    login_required()
    animalForRemoval = session.query(Animal).filter_by(id=animal_id).one()
    if animalForRemoval.user_id != login_session['user_id']:
        flash('You are not authorized to edit this animal.'
              'Please create your own animal in order to add, edit or remove.')
        return redirect(url_for('showAnimals'))
    if request.method == 'POST':
        session.delete(animalForRemoval)
        session.commit()
        flash('%s successfully deleted!' % animalForRemoval.name)
        return redirect(url_for('showAnimals', animal_id=animal_id))
    else:
        return render_template('deleteAnimal.html', animal=animalForRemoval)


@app.route('/animal/<int:animal_id>/')
@app.route('/animal/<int:animal_id>/toys/')
def showToys(animal_id):
    animal = session.query(Animal).filter_by(id=animal_id).one()
    creator = getUserInfo(animal.user_id)
    toys = session.query(Toy).filter_by(animal_id=animal_id).all()
    if 'username' not in login_session or creator.id != login_session['user_id']:
        return render_template('publicToys.html',
                                toys=toys,
                                animal=animal,
                                creator=creator)
    else:
        return render_template('toys.html',
                                toys=toys,
                                animal=animal,
                                creator=creator)


@app.route('/animal/<int:animal_id>/toys/new/', methods=['GET', 'POST'])
def newToy(animal_id):
    login_required()
    animal = session.query(Animal).filter_by(id=animal_id).one()
    if login_session['user_id'] != animal.user_id:
        flash('You are not authorized to add toys for this animal.'
              'Please create your own animal in order to add, edit or remove.')
        return redirect(url_for('showToys', animal_id=animal_id))
    if request.method == 'POST':
        newToy = Toy(name=request.form['name'],
                     toy_type=request.form['toy_type'],
                     description=request.form['description'],
                     photo=request.form['photo'],
                     user_id=animal.user_id,
                     animal_id=animal_id)
        session.add(newToy)
        session.commit()
        flash('%s successfully created!' % newToy.name)
        return redirect(url_for('showToys', animal_id=animal_id))
    else:
        return render_template('newToy.html', animal_id=animal_id)


@app.route('/animal/<int:animal_id>/toys/<int:toy_id>/edit/',
            methods=['GET', 'POST'])
def editToy(animal_id, toy_id):
    login_required()
    editedToy = session.query(Toy).filter_by(id=toy_id).one()
    animal = session.query(Animal).filter_by(id=animal_id).one()
    if login_session['user_id'] != animal.user_id:
        flash('You are not authorized to edit this toy.'
              'Please create your own animal in order to add, edit or remove.')
        return redirect(url_for('showToys', animal_id=animal_id))
    if request.method == 'POST':
        if request.form['name']:
            editedToy.name = request.form['name']
        if request.form['toy_type']:
            editedToy.toy_type = request.form['toy_type']
        if request.form['description']:
            editedToy.description = request.form['description']
        if request.form['photo']:
            editedToy.photo = request.form['photo']
        session.add(editedToy)
        session.commit()
        flash('%s successfully edited!' % editedToy.name)
        return redirect(url_for('showToys', animal_id=animal_id))
    else:
        return render_template('editToy.html',
                                animal_id=animal_id,
                                toy_id=toy_id,
                                toy=editedToy)


@app.route('/animal/<int:animal_id>/toys/<int:toy_id>/delete/',
            methods=['GET', 'POST'])
def deleteToy(animal_id, toy_id):
    login_required()
    animal = session.query(Animal).filter_by(id=animal_id).one()
    toyForRemoval = session.query(Toy).filter_by(id=toy_id).one()
    if login_session['user_id'] != animal.user_id:
        flash('You are not authorized to edit this toy.'
              'Please create your own animal in order to add, edit or remove.')
        return redirect(url_for('showToys', animal_id=animal_id))
    if request.method == 'POST':
        session.delete(toyForRemoval)
        session.commit()
        flash('%s successfully deleted!' % toyForRemoval.name)
        return redirect(url_for('showToys', animal_id=animal_id))
    else:
        return render_template('deleteToy.html',
                                animal_id=animal_id,
                                toy_id=toy_id,
                                toy=toyForRemoval)


if __name__ == '__main__':
    app.secret_key = 'secret_key_!@#'
    app.debug = True
    # Bind to PORT if defined, otherwise default to 8030.
    port = int(os.environ.get('PORT', 8030))
    app.run(host='0.0.0.0', port=port)
