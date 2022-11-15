# -*- coding: utf-8 -*-
import json
from pyop.access_token import AccessToken
from flask import current_app, make_response
import requests
#from authlib.oauth2.rfc6749 import (HttpRequest, MissingAuthorizationError, UnsupportedTokenTypeError)
from flask import request
from settings import *

def token_required(scope=None):
    def decorator(function):
        def wrapper(*args, **kwargs):

            try:
                if DECORADOR_ACTIVE:
                    # request = HttpRequest(
                    #     _req.method,
                    #     _req.full_path,
                    #     _req.data,
                    #     _req.headers
                    # )
                    id_empresa = request.headers.get('idempresa')
                    id_pais = request.headers.get('idpais')
                    id_sistema = request.headers.get('idsistema')
                    trace_id = request.headers.get('traceid')

                    if not id_empresa or not id_pais or not id_sistema:
                        return make_response({'success': False,
                                            'message': 'Error, falta la cabecera de idempresa, idpais, idsistema'}, 401)
            except Exception as e:
                response = make_response({'success': False, 'message': str(e)}, 401)
                # response.headers['WWW-Authenticate'] = AccessToken.BEARER_TOKEN_TYPE
                # response.headers['Content-Type'] = 'application/json'
                return response

            result = function(*args, **kwargs)
            return result

        wrapper.__name__ = function.__name__
        return wrapper

    return decorator
