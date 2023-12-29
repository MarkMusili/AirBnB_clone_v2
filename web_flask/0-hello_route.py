#!/usr/bin/python3
"""This module/app initiates web server using flask"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
	"""Function to return a string"""
	return 'Hello HBNB!'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)