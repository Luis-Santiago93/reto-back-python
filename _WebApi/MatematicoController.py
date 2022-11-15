from flask import Blueprint, request, jsonify
from Domain.DomainServices.MatematicoDomain import MatematicoDomain
from Domain.Settings_Domain import *
from Domain.Utils.response import json_response
from settings import create_app, ENVIRONMENT_NAME
from marshmallow import ValidationError

app = create_app(ENVIRONMENT_NAME)
context = app.config["CONTEXT_FACTORY"](app, False)
matematico_controller = Blueprint("MatematicoController", __name__,url_prefix='/api/v1.0')
_matematico_domain = MatematicoDomain(context=context)

@matematico_controller.get("/minimo_multipo")
def get_minimo_multiplo():
    numbers = request.args.getlist('numbers[]')
    if not numbers:
        return json_response(success=False, message=PARAMETERS_ID)
    response = _matematico_domain.get_minimo_multiplo(numbers)
    return jsonify(response['data']), response['code']

@matematico_controller.get("/sumatoria")
def sum():
    number = request.args.get('number')
    if not number:
        return json_response(success=False, message=PARAMETERS_ID)
    response = _matematico_domain.sum(number)
    return jsonify(response['data']), response['code']