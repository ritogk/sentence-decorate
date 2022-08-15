#!/usr/bin/python3 

from flask import Flask
from service.spacy import Spacy
from flask import Flask, make_response, request, jsonify

app = Flask(__name__)
spacy = Spacy()

server_domain = 'http://server.test.com:5000'

@app.route("/")
def index():
    sentents = request.args.get('sentents')
    sentens_analays = spacy.sentents_to_doc(sentents)
    response = make_response(jsonify(sentens_analays), 200)
    response.headers.set('Content-Type', 'aplication/json')
    response.headers.add('X-Content-Type-Options', 'nosniff')
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET')
    return response
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)