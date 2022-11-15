from flask import Blueprint, request, jsonify
from Domain.DomainServices.ChistesDomain import ChistesDomain
from Domain.Settings_Domain import *
from Infrastructure.Entities.Core.Chistes import chistes_schema
from Domain.Utils.response import json_response
from Domain.Utils.token_sec import token_required
from settings import create_app, ENVIRONMENT_NAME
from marshmallow import ValidationError
from Infrastructure.Repositories.Complements.Utils import validate_duplicates

app = create_app(ENVIRONMENT_NAME)
context = app.config["CONTEXT_FACTORY"](app, False)
chistes_controller = Blueprint("ChistesController", __name__,url_prefix='/api/v1.0')
_chistes_domain = ChistesDomain(context=context)

@chistes_controller.get("/joke/<id>")
@token_required()
def get_by_id(id):
    response = _chistes_domain.get_by_id(id)
    return jsonify(response['data']), response['code']

@chistes_controller.get("/joke")
def get_all_chistes():
    response = _chistes_domain.get_all_chistes()
    return jsonify(response['data']), response['code']

@chistes_controller.get("/joke_type/<type>")
@token_required()
def get_chistes(type):
    print('servicio')
    print(type)
    response = _chistes_domain.get_chistes(type)
    return jsonify(response['data']), response['code']

@chistes_controller.post("/joke")
@token_required()
def insert():
    received = request.json

    schema = chistes_schema()
    try:
        result_validation = schema.load(received)
        return jsonify(_chistes_domain.insert(result_validation))
    except ValidationError as err:
        return json_response(success=False, message=err.messages)

@chistes_controller.put("/joke")
@token_required()
def update():
    received = request.json

    schema = chistes_schema()
    try:
        if 'id' not in received:
            return json_response(success=False, message=REQUIERED_UPDATE)
        result_validation = schema.load(received)
        return jsonify(_chistes_domain.update(result_validation))
    except ValidationError as err:
        return json_response(success=False, message=err.messages)
    
@chistes_controller.delete('/joke')
@token_required()
def delete():
    received = request.json
    if 'id' not in received:
        return json_response(success=False, message=REQUIERED_UPDATE)
    id = received['id']
    return jsonify(
        _chistes_domain.delete(id)
    )