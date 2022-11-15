from flask.json import jsonify
from Domain.Utils.response import json_response, json_error_response
from Domain.Settings_Domain import *
import datetime

class MatematicoDomain():
    _matematica_repository = None

    def __init__(self, context):
        self._matematica_repository = context.context_matematica_repository
        super().__init__()

    def get_minimo_multiplo(self, numbers):
        try:
            i = self._matematica_repository.get_minimo_multiplo(numbers)
            if i is None:
                return {'data':json_response(success=False, message=ERROR_PROCESS),'code':404 }
            return {'data':json_response(data=i, success=True, message=JOB_EXECUTED),'code':200 }

        except Exception as e:
            return json_error_response(e)
    
    def sum(self, number):
        try:
            i = self._matematica_repository.sum(number)
            if i is None:
                return {'data':json_response(success=False, message=ERROR_PROCESS),'code':404 }
            return {'data':json_response(data=i, success=True, message=JOB_EXECUTED),'code':200 }

        except Exception as e:
            return {'data':json_error_response(e),'code':404 }