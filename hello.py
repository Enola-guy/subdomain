# coding: utf-8
from flask import Flask
import sublist3r as sub

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


