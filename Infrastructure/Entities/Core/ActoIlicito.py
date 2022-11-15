from marshmallow import Schema, fields, validate, post_load
from Domain.DomainServices.DomainBase import BaseSchema
# from marshmallow_validators.wtforms import from_wtforms
# from wtforms.validators import InputRequired, Length


class acto_ilicito(object):
    
    def __init__(self, id = None,actividad_id = None,danio_equipo = None, costo_produccion_diferida = None,
        fecha_creacion = None,creado_por = None,fecha_modificacion = None,modificado_por = None, vigente = None):
        self.id = id
        self.actividad_id = actividad_id
        self.danio_equipo = danio_equipo
        self.costo_produccion_diferida = costo_produccion_diferida
        self.fecha_creacion = fecha_creacion
        self.creado_por = creado_por
        self.fecha_modificacion = fecha_modificacion
        self.modificado_por = modificado_por
        self.vigente = vigente
        
    def __repr__(self):
        return "acto_ilicito Object (Id='%s')" % self.id


# locales = ['es_ES', 'es']

class ActoIlicitoSchema(BaseSchema):
    id = fields.Integer()
    actividad_id = fields.Integer(required = True)
    danio_equipo = fields.String()
    costo_produccion_diferida  =fields.Decimal(places=2)
    vigente = fields.Boolean(missing=True)

    @post_load
    def make_acto_ilicito(self, data, **kwargs):
        return acto_ilicito(**data)
