#!/usr/bin/env python3
"""This is the hello module"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """Display Hello HBNB!"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HB"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Display of c is fun"""
    text = text.replace("_", " ")
    return "C " + text

@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """Display of c is fun"""
    text = text.replace("_", " ")
    return "Python " + text

if (__name__) == "__main__":
    app.run(host='0.0.0.0', port=5000)
