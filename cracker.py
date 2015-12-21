#!/usr/bin/env python

from flask import Flask
from string import digits, ascii_uppercase, ascii_lowercase
from itertools import product

app = Flask(__name__)


@app.route('/')
def hello_world():
    chars = digits + ascii_uppercase + ascii_lowercase
    combinations = []

    for n in range(3, 5):
        for combination in product(chars, repeat=n):
            str_combination = ''.join(combination)
            combinations.append(str_combination)

    return "Hello"

if __name__ == '__main__':
    app.run(host='192.168.0.94', debug=True)
