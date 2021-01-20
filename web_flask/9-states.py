#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def tear_down(exception):
    """
    remove the current SQLAlchemy Session
    """
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def display_states(id=''):
    """
    display states and states with id
    """
    states = storage.all(State)
    return render_template('9-states.html', states=states, id=id)


if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
