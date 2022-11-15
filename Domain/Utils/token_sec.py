# -*- coding: utf-8 -*-
import json
from pyop.access_token import AccessToken
from flask import current_app, make_response
import requests
from authlib.oauth2.rfc6749 import (HttpRequest, MissingAuthorizationError, UnsupportedTokenTypeError)
from flask import request as _req
from settings import *

config = config_by_name[ENVIRONMENT_NAME]
URL_SSO = config.URL_SSO
VERIFY_SSL = config.VERIFY_SSL


def getToken():
    if DECORADOR_ACTIVE:
        from flask import request
        auth = request.headers.get('Authorization')
        if not auth:
            raise MissingAuthorizationError()
        token_parts = auth.split(None, 1)
        if len(token_parts) != 2:
            raise UnsupportedTokenTypeError()
        token_type, token_string = token_parts
        return token_string
    return ''


def token_required(scope=None):
    def decorator(function):
        def wrapper(*args, **kwargs):

            try:
                if DECORADOR_ACTIVE:
                    request = HttpRequest(
                        _req.method,
                        _req.full_path,
                        _req.data,
                        _req.headers
                    )
                    auth = request.headers.get('Authorization')
                    if not auth:
                        return make_response({'success': False,
                                              'message': 'Error, falta la cabecera de autorización'}, 401)
                    token_parts = auth.split(None, 1)
                    if len(token_parts) != 2:
                        return make_response({'success': False,
                                              'message': 'Tipo de token no soportado'}, 401)

                    token_type, token_string = token_parts
                    tokencad = tokenIntrospection(token_string)
                    json_introspection = json.loads(tokencad)
                    if 'error' in json_introspection:
                        return make_response({'success': False,
                                              'message': 'Token invalido'}, 401)

                    active = False
                    if isinstance(json_introspection, dict) and 'active' in json_introspection:
                        active = json_introspection['active']

                    if not active:
                        return make_response({'success': False,
                                              'message': 'Token invalido'}, 401)
                    if scope:
                        scopeFromParams = scope
                        scopesSpliteado = json_introspection['scope'].split()
                        scopesFromLookupKey = get_by_lookup_key(token_string)

                        scopesSpliteado = list(set().union(scopesSpliteado, scopesFromLookupKey))

                        if not scopeFromParams in scopesSpliteado:
                            return make_response({'success': False,
                                                  'message': 'No tiene permisos para ejecutar esta accion'}, 401)

            except Exception as e:
                response = make_response({'success': False, 'message': str(e)}, 401)
                response.headers['WWW-Authenticate'] = AccessToken.BEARER_TOKEN_TYPE
                response.headers['Content-Type'] = 'application/json'
                return response

            result = function(*args, **kwargs)
            return result

            wrapper.__name__ = function.__name__

        wrapper.__name__ = function.__name__
        return wrapper

    return decorator


def get_by_lookup_key(token):
    resp = requests.post(url=URL_SSO + '/api/v1.0/scope/getbylookupkey', data={'token': token}, headers={
        'Authorization': f'Bearer {token}'
    }, verify = VERIFY_SSL)
    return [item['Name'] for item in json.loads(resp.text)['data']]


def tokenIntrospection(token):
    resp = requests.post(url=URL_SSO + '/introspection', data={'token': token}, headers={
        'Authorization': 'Bearer %s' % token
    }, verify = VERIFY_SSL)
    return resp.text
