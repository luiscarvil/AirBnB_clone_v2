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
    display: Hello HBNB
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
