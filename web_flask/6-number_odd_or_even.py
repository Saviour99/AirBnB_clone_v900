#!/usr/bin/env python3
"""This is the hello module"""

from flask import Flask, render_template

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

@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
        return f"{n} is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    parity = "even" if n % 2 == 0 else "odd"
    return render_template('number_odd_or_even.html', n=n, parity=parity)

if (__name__) == "__main__":
    app.run(host='0.0.0.0', port=5000)
