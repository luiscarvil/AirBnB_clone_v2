#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def tear_down(exception):
    """
    remove the current SQLAlchemy Session
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def display_filters():
    """
    State, City and Amenity objects must be loaded from DBStorage
    """
    amenities = storage.all(Amenity)
    states = storage.all(State)
    return render_template('10-hbnb_filters.html',
                           amenities=amenities, states=states)


if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
