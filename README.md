# Zoo Toy Tracker (Item Catalog Project)
Source code for an application that supports creating, editing, and deleting various items in a database.

## Summary
This is a project for the Udacity Full Stack Web Development Nanodegree. This project is a web application that was built using Python on the Flask framework for the server code, and SQLAlchemy for the database operations. It also makes use of OAuth with Google's API for user authentication(Google Sign-in).

The target user base of this application is zoo keepers and other zoo personnel. It provides a database in which they can manage(add, edit, delete) several animals and each animal's toys(a.k.a enrichment devices).

## Contents
This application is made up of several files, most being templates:
- `project.py` Web server, template rendering, and routing is all done here.
- `database_setup.py` Database schema defined here, and will create `animal_toys.db`.
- `client_secrets.json` Provides the client ID and client secret from Google for use with OAuth.
- `templates/` Contains all HTML templates. Each file's name should be self-explanatory.
- `static/` Contains the single style file: `style.css`.

## Requirements
The Python used in this project was version 2.7.13. If you're having issues running this code with another version, download this version [here](https://www.python.org/downloads/), and try it again.

## Usage
Before you start the application, you'll want to run a few files first:
1. Clone this repository.
2. Navigate to this project's directory in the python shell.
3. Run `database_setup.py`.
5. Run `project.py`.
6. In a browser(preferably Chrome), go to `localhost:5000`(If port 5000 is occupied on your machine, change the port for the web server at the bottom of the `project.py` file).

You should first see only the Google Sign-in page. If you want to skip this, navigate to localhost:5000/animals. The 'animals' page acts as the Home page. Keep in mind, if you skip login, this application will be a read-only one in that you cannot add, edit, or delete any items; you can only view.
