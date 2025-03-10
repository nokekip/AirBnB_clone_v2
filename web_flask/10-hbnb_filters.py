#!/usr/bin/python3
"""
Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /hbnb_filters: HBnB HTML filters page.
"""


from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask
from flask import render_template, url_for


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """ Displays the main HBnB filters HTML page. """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html", states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """ Remove current Database session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
