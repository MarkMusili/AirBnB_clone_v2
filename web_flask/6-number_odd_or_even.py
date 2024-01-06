#!/usr/bin/python3
"""This module/app initiates web server using flask"""
from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Function to return a string"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Function to return a string"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Function to return a string"""
    text = escape(text.replace('_', ' '))
    return f'C {text}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """Function to return a string"""
    text = escape(text.replace('_', ' '))
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """Function to check for a number"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_number(n):
    """Function to check for a number"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def template_number_odd_even(n):
    """Function to check for a number"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)