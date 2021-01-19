#!/usr/bin/python3
"""
starts Flask web application lintening on 0.0.0.0, port 5000
"""
from flask import Flask

"""
flask class
"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def starts_flask():
    """
    display: Hello HBNB!
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def starts_flask_hbtn():
    """
    display: HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_C(text):
    """
    return display C: value of the text variable
    (replace underscore _ symbols with a space )
    """
    return "C {:s}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_Python(text="is cool"):
    """
    return display python: value of the text variable
    (replace underscore _ symbols with a space )
    """
    return "Python {:s}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def display_int(n):
    """
    return display int: integer
    """
    if isinstance(n, int):
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
