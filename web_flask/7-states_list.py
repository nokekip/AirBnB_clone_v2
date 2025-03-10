#!/usr/bin/python3
"""
Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /states_list:A HTML page with a list of all State objects in DBStorage.
"""

from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    Displats a HTML page with a list of all State objects in DBStorage.
    States are sorted by name.
    """
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def tearsown(exc):
    """ Remove current Database session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
