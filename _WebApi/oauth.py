import requests
from authlib.integrations.flask_client import OAuth
from flask import Blueprint, request, url_for, session, redirect
from Domain.Utils.response import json_response, json_error_response
from Domain.Utils.no_ssl_verification import no_ssl_verification
from Domain.Utils.token_sec import getToken
from settings import *

app = create_app(ENVIRONMENT_NAME)
oauth = OAuth(app)

OPPEMEX_CLIENT_ID = app.config['OPPEMEX_CLIENT_ID']
OPPEMEX_CLIENT_SECRET = app.config['OPPEMEX_CLIENT_SECRET']
URL_APP = app.config['URL_APP']
URL_SSO = app.config['URL_SSO']
MY_URL = app.config['MY_URL']
SCOPES = app.config['SCOPES']
TOKEN_NAME = app.config['TOKEN_NAME']
VERIFY_SSL = app.config["VERIFY_SSL"]


oauth.init_app(app)
with no_ssl_verification():
    oauth.register(
        'oppemex',
        server_metadata_url=URL_SSO + '/.well-known/openid-configuration',
        client_kwargs={'scope': SCOPES}
    )

OAUTHController = Blueprint("OAUTHController", __name__)


@OAUTHController.route('/login', methods=['GET'])
def login():
    url = request.values.get("url") or request.headers.get("Referer")
    if url:
        session['post_login_referer'] = url
    alt_url = MY_URL + '/auth'
    redirect_uri = url_for('OAUTHController.auth', _external=True)
    if MY_URL not in redirect_uri:
        redirect_uri = alt_url
    with no_ssl_verification():
        return oauth.oppemex.authorize_redirect(redirect_uri)


@OAUTHController.route('/logout')
def logout():
    if TOKEN_NAME in session:
        token = session[TOKEN_NAME]

    if TOKEN_NAME in session:
        id_token = session[TOKEN_NAME]['id_token']
        if id_token is not None:
            # session.pop(TOKEN_NAME, None)
            # session.pop('id_token', None)
            response = redirect(
                URL_SSO + '/logout?id_token_hint=' + id_token + '&post_logout_redirect_uri=' + URL_APP)
            # response.delete_cookie('pythoken')
            return response

    response = redirect(URL_APP)
    return response


@OAUTHController.route('/auth')
def auth():
    with no_ssl_verification():
        token = oauth.oppemex.authorize_access_token()
        id_token = oauth.oppemex.parse_id_token(token)
        session['id_token'] = id_token
        session[TOKEN_NAME] = token
    response = None
    if token['access_token'] is not None:
        redirect_final = URL_APP
        response = redirect(redirect_final, 303)
        domain = app.config['SESSION_COOKIE_DOMAIN'] or None
        secure = app.config['SESSION_COOKIE_SECURE'] or None
        samesite = app.config['SESSION_COOKIE_SAMESITE'] or None
        if app.config['SESSION_COOKIE_BAND']:
            response.set_cookie(key=TOKEN_NAME, value=token['access_token'], samesite=samesite,
                                domain=domain, secure=secure)
        else:
            response.set_cookie(key=TOKEN_NAME, value=token['access_token'])

    return response


@OAUTHController.route('/userinfo')
def userinfo():
    token = getToken()
    headers = {'Authorization': 'Bearer ' + token}
    ret = requests.get(URL_SSO + '/userinfo', headers=headers, verify = VERIFY_SSL)
    if ret.status_code not in (200, 201):
        return ret.content, ret.status_code
    return ret.content


@OAUTHController.route('/role_scope_user_info', methods=['POST'])
def token_info_by_lookupkey():
    try:
        token = getToken()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }
        ret = requests.post(URL_SSO + '/api/v1.0/roleuserscope/token_info',
                            headers=headers,
                            json={'client_id': OPPEMEX_CLIENT_ID}, verify = VERIFY_SSL)

        if ret.status_code not in (200, 201):
            return ret.content, ret.status_code
        r = ret.json()
        return r
    except Exception as e:
        return json_error_response(e)


@OAUTHController.route('/echo', methods=['POST'])
def echo():
    try:
        token = getToken()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }
        ret = requests.post(URL_SSO + '/echo', headers=headers, verify = VERIFY_SSL)
        if ret.status_code not in (200, 201):
            return ret.content, ret.status_code
        r = ret.json()
        return r
    except Exception as e:
        return json_response(success=False, message='Token no valido')


@OAUTHController.route('/get_ticket', methods=['POST'])
def get_ticket():
    try:
        if request.json.get('username', '') != '':
            username = request.json.get('username', '')
        if request.json.get('password', '') != '':
            password = request.json.get('password', '')
        data = {
            'username': username,
            'password': password,
            'client_id': OPPEMEX_CLIENT_ID
        }
        ret = requests.post(URL_SSO + '/get_ticket', json=data, verify = VERIFY_SSL)
        if ret.status_code not in (200, 201):
            return ret.content, ret.status_code
        r = ret.json()
        return r
    except Exception as e:
        return json_response(success=False, message='Ocurrio un error', data=r)


@OAUTHController.route('/ping', methods=['POST', 'GET'])
def checking():
    if not session:
        return json_response(success=True, message=f'no existe session')
    if TOKEN_NAME in session:
        return json_response(success=True, message=f'pong..{TOKEN_NAME}')
    if 'pythoken' in session:
        return json_response(success=True, message=f'pong..pythoken')
    else:
        return json_response(success=True, message=f'token name not in session')