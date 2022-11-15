from abc import ABC, abstractmethod
from marshmallow import Schema, fields, validate
import datetime

class DomainBase(ABC):
    def __init__(self):
        pass

    def get_by_id(self, id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def insert(self, item):
        pass

    @abstractmethod
    def delete(self, item):
        pass

    @abstractmethod
    def update(self, item):
        pass

class BaseSchema(Schema):
    usuario_creacion = fields.String(validate=validate.Length(min=4))
    usuario_ult_modif = fields.String(validate=validate.Length(min=4))