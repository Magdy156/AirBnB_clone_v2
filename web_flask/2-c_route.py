#!/usr/bin/python3
"""Adding another hello func"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ Returns Hello world """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello():
    """ Return HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def CText(text):
    """Route with parameter"""
    string = text.replace('_', ' ')
    return f'C {string}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
