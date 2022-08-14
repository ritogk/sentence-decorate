#!/usr/bin/python3 

from flask import Flask
from service.spacy import Spacy
app = Flask(__name__)
spacy = Spacy()

@app.route("/")
def index():
    return spacy.html_to_doc('html')
    return "index page"