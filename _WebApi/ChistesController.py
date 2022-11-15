from flask import Blueprint, request, jsonify
from Domain.DomainServices.ChistesDomain import ChistesDomain
from Domain.Utils.response import json_response
from Domain.Settings_Domain import *
from settings import create_app, ENVIRONMENT_NAME

app = create_app(ENVIRONMENT_NAME)
context = app.config["CONTEXT_FACTORY"](app, False)
chistes_controller = Blueprint("ChistesController", __name__,url_prefix='/api/v1.0')
_chistes_domain = ChistesDomain(context=context)

@chistes_controller.get("/joke")
def get_all_chistes():
    response = _chistes_domain.get_all_chistes()
    return jsonify(response['data']), response['code']

@chistes_controller.get("/joke/<type>")
def get_chistes(type):
    print(type)
    response = _chistes_domain.get_chistes(type)
    return jsonify(response['data']), response['code']

