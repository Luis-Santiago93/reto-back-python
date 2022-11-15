from flask.json import jsonify
from Domain.DomainServices.DomainBase import DomainBase
from Domain.Utils.response import json_response, json_error_response
from Domain.Settings_Domain import *
import datetime
import random

class ChistesDomain(DomainBase):
    _chistes_repository = None

    def __init__(self, context):
        self._chistes_repository = context.context_chistes_repository
        super().__init__()

    def get_chistes(self, type):
        try:
            if type.lower()=='chuck':
                joke_chuck = self._chistes_repository.get_api_chucknorris()
                if joke_chuck is None:
                    return {'data':json_response(success=False, message=ROW_NOT_FOUND),'code':404 }
                return {'data':json_response(data=joke_chuck, success=True, message=SUCCESSFUL_CONSULTATION),'code':200 }
            elif type.lower()=='dad':
                joke = self._chistes_repository.get_api_joke()
                if joke is None:
                    return {'data':json_response(success=False, message=ROW_NOT_FOUND),'code':404 }
                return {'data':json_response(data=joke, success=True, message=SUCCESSFUL_CONSULTATION),'code':200 }
            else:
                return {'data':json_response(success=False, message=ERROR_PARAMETERS),'code':404 }
        except Exception as e:
            return json_error_response(e)
        
    def get_all_chistes(self):
        try:
            apis_jokes = [self._chistes_repository.get_api_joke, self._chistes_repository.get_api_chucknorris]
            select_api=random.choice(apis_jokes)()
            if select_api is None:
                return {'data':json_response(success=False, message=ROW_NOT_FOUND),'code':404 }
            return {'data':json_response(data=select_api, success=True, message=SUCCESSFUL_CONSULTATION),'code':200 }
        except Exception as e:
            return json_error_response(e)
        
    def get_by_id(self, id):
        try:
            i = self._chistes_repository.get_by_id(id)
            if i is None:
                return {'data':json_response(success=False, message=ROW_NOT_FOUND),'code':404 }
            return {'data':json_response(data=i, success=True, message=SUCCESSFUL_CONSULTATION),'code':200 }

        except Exception as e:
            return json_error_response(e)
    
    def get_by_producto(self, id,version):
        try:
            i = self._chistes_repository.get_by_producto(id, version)
            if not i:
                return {'data':json_response(success=False, message=ZERO_ROWS),'code':404 }
            
            return {'data':json_response(data=i, success=True, message=SUCCESSFUL_CONSULTATION),'code':200 }

        except Exception as e:
            return {'data':json_error_response(e),'code':404 }

    def get_all(self):
        try:
            all_rows = self._chistes_repository.get_all()
            if not all_rows:
                return {'data':json_response(success=False, message=ZERO_ROWS),'code':404 }
            
            return {'data':json_response(data=all_rows, success=True, message=SUCCESSFUL_CONSULTATION),'code':200 }
        except Exception as e:
            return {'data':json_error_response(e),'code':404 }

    def insert(self, item):
        try:
            item.fecha_creacion=datetime.datetime.now()
            all_rows = self._chistes_repository.insert(item)
            if not all_rows:
                return json_response(success=False, message=ERROR_INSERT)
            return json_response(data=all_rows, success=True, message=ROW_INSERTED)
        except Exception as e:
            return json_error_response(e)

    def delete(self, id):
        try:
            i = self._chistes_repository.get_by_id(id)
            if i is None:
                return json_response(success=False, message=ROW_NOT_FOUND)
            self._chistes_repository.delete(id)
            return json_response(success=True, message=ROW_DELETE)
        except Exception as e:
            return json_error_response(e)
    
    def update(self, item):
        try:
            i = self._chistes_repository.get_by_element(item.id)
            if i is None:
                return json_response(success=True, message=ROW_NOT_FOUND)
            item.fecha_creacion = i.fecha_creacion
            item.fecha_modificacion = datetime.datetime.now()
            row=self._chistes_repository.update(item)
            if not row:
                return json_response(success=False, message=ERROR_PROCESS)
            else:                
                return json_response(data=row, success=True, message=ROW_UPDATED)
        except Exception as e:
            return json_error_response(e)

    def disabled(self, id):
        try:
            i = self._chistes_repository.get_by_id(id)
            if i is None:
                return json_response(success=True, message=ROW_NOT_FOUND)
            if self._chistes_repository.disabled(id):
                return json_response(success=True, message=ROW_UPDATED)
        except Exception as e:
            return json_error_response(e)