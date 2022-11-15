from flask.json import jsonify
from Domain.DomainServices.DomainBase import DomainBase
from Domain.Utils.response import json_response, json_error_response
from Domain.Settings_Domain import *
import datetime
class ActoIlicitoDomain(DomainBase):
    _acto_ilicito_repository = None

    def __init__(self, context):
        self._acto_ilicito_repository = context.context_acto_ilicito_repository
        super().__init__()

    def get_by_id(self, id):
        try:
            i = self._acto_ilicito_repository.get_by_id(id)
            if i is None:
                return json_response(success=True, message=ROW_NOT_FOUND)
            return json_response(data=i, success=True, message=SUCCESSFUL_CONSULTATION)

        except Exception as e:
            return json_error_response(e)
    
    def get_by_evento(self, id):
        try:
            i = self._acto_ilicito_repository.get_by_evento(id)
            if i is None:
                return {'data':json_response(success=False, message=ROW_NOT_FOUND),'code':404 }
            
            return {'data':json_response(data=i, success=True, message=SUCCESSFUL_CONSULTATION),'code':200 }

        except Exception as e:
            return {'data':json_error_response(e),'code':404 }

    def get_all(self):
        try:
            all_rows = self._acto_ilicito_repository.get_all()
            if not all_rows:
                return {'data':json_response(success=False, message=ZERO_ROWS),'code':404 }
            
            return {'data':json_response(data=all_rows, success=True, message=SUCCESSFUL_CONSULTATION),'code':200 }
        except Exception as e:
            return {'data':json_error_response(e),'code':404 }

    def insert(self, item):
        try:
            item.fecha_creacion=datetime.datetime.now()
            all_rows = self._acto_ilicito_repository.insert(item)
            if not all_rows:
                return json_response(success=False, message=ERROR_INSERT)
            return json_response(data=all_rows, success=True, message=ROW_INSERTED)
        except Exception as e:
            return json_error_response(e)

    def delete(self, id):
        pass
        # try:
        #     i = self._investigacion_grupo_trabajo_repository.get_by_id(id)
        #     if i is None:
        #         return json_response(success=False, message=ROW_NOT_FOUND)
        #     if self._investigacion_grupo_trabajo_repository.delete(id):
        #         return json_response(success=True, message=ROW_DELETED)
        # except Exception as e:
        #     return json_error_response(e)
    
    def update(self, item):
        try:
            i = self._acto_ilicito_repository.get_by_element(item.id)
            if i is None:
                return json_response(success=True, message=ROW_NOT_FOUND)
            item.fecha_creacion = i.fecha_creacion
            item.creado_por = i.creado_por
            item.fecha_modificacion = datetime.datetime.now()
            if self._acto_ilicito_repository.update(item,item.id):
                return json_response(success=True, message=ROW_UPDATED)
        except Exception as e:
            return json_error_response(e)

    def disabled(self, id):
        try:
            i = self._acto_ilicito_repository.get_by_id(id)
            if i is None:
                return json_response(success=True, message=ROW_NOT_FOUND)
            if self._acto_ilicito_repository.disabled(id):
                return json_response(success=True, message=ROW_UPDATED)
        except Exception as e:
            return json_error_response(e)