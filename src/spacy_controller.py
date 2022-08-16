from service.spacy_service import SpacyService
from flask import make_response, jsonify, Response

spacy_service = SpacyService()

server_domain = 'http://server.test.com:5000'

class SpacyController:
  def get(self, sentents: str) -> Response:
    sentents_analyses = spacy_service.sentents_to_doc(sentents)
    response = make_response(jsonify(sentents_analyses), 200)
    response.headers.set('Content-Type', 'aplication/json')
    response.headers.add('X-Content-Type-Options', 'nosniff')
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET')
    return response

