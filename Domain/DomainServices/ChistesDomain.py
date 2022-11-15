from Domain.Utils.response import json_response, json_error_response
from Domain.DomainServices.DomainBase import DomainBase
from Domain.Settings_Domain import *
import random

class ChistesDomain(DomainBase):
    _chistes_repository = None

    def __init__(self, context):
        self._chistes_repository = context.context_chistes_repository
        super().__init__()

    def get_all(self):
        pass
        
    def get_chistes(self, type):
        try:
            if type=='Chuck':
                joke_chuck = self._chistes_repository.get_api_chucknorris()
                if joke_chuck is None:
                    return {'data':json_response(success=False, message=ROW_NOT_FOUND),'code':404 }
                return {'data':json_response(data=joke_chuck, success=True, message=SUCCESSFUL_CONSULTATION),'code':200 }
            elif type=='Dad':
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
        
    def insert(self, item):
        pass

    def delete(self, id):
        pass
    
    def update(self, item):
        pass
