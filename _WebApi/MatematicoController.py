from flask import Blueprint, request, jsonify
from Domain.DomainServices.ActoIlicitoDomain import ActoIlicitoDomain
from Domain.Utils.token_sec import token_required
from Domain.Settings_Domain import *
from Domain.Utils.response import json_response
from Infrastructure.Entities.Core.ActoIlicito import  ActoIlicitoSchema, acto_ilicito
from marshmallow import ValidationError
from settings import create_app, ENVIRONMENT_NAME


app = create_app(ENVIRONMENT_NAME)
context = app.config["CONTEXT_FACTORY"](app, False)
acto_ilicito_controller = Blueprint("ActoIlicitoController", __name__,url_prefix='/api/v1.0')
_acto_ilicito_domain = ActoIlicitoDomain(context=context)

def set_disabled(received):
    item = acto_ilicito(
        id=received['id']
    )
    return item

@acto_ilicito_controller.get("/ActoIlicito/<id>")
def get_by_id(id):
    return jsonify(_acto_ilicito_domain.get_by_id(id)), 200

@acto_ilicito_controller.get("/ActoIlicito/Evento/<id>")
#@token_required()
def get_by_evento(id):
    response = _acto_ilicito_domain.get_by_evento(id)
    return jsonify(response['data']), response['code']

@acto_ilicito_controller.get("/ActoIlicito")
def get_all():
    response = _acto_ilicito_domain.get_all()
    return jsonify(response['data']), response['code']

@acto_ilicito_controller.post("/ActoIlicito")
def insert():
    received = request.json
  
    schema = ActoIlicitoSchema()
    try:
        if 'actividad_id' not in received or 'creado_por' not in received:
            return json_response(success=False, message=PARAMETERS_REQUIERED_INSERT)

        result_validation = schema.load(received)
    
        return jsonify(_acto_ilicito_domain.insert(result_validation))
    except ValidationError as err:
        return json_response(success=False, message=err.messages)
            
@acto_ilicito_controller.put("/ActoIlicito")
def update():
    received = request.json

    schema = ActoIlicitoSchema()
    try:
        if 'id' not in received or 'actividad_id' not in received or 'modificado_por' not in received:
            return json_response(success=False, message=PARAMETERS_REQUIERED_UPDATE)

        result_validation = schema.load(received)

        return jsonify(_acto_ilicito_domain.update(result_validation))
    except ValidationError as err:
        return json_response(success=False, message=err.messages)


@acto_ilicito_controller.patch("/ActoIlicito/Inactivo")
def disabled():
    received = request.json
    if 'id' not in received:
        return json_response(success=False, message=ID_REQUIERED)
    item = set_disabled(received)
    return jsonify(_acto_ilicito_domain.disabled(item.id))