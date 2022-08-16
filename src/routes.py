from flask import Blueprint, request
from controllers.spacy_controller import SpacyController
routes = Blueprint("routes", __name__)

spacy_controller = SpacyController()

@routes.route("/spacy")
def index():
    sentents = request.args.get('sentents')
    return spacy_controller.get(sentents)