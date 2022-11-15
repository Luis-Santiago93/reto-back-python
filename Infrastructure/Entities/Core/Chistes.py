from marshmallow import Schema,fields,post_load

class Chistes(object):
    def __init__(self,
        id=None,
        descripcion = None,
        fecha_creacion =None,
        fecha_ult_modif =None,
        vigente=None
        ):

        self.id = id
        self.descripcion = descripcion
        self.fecha_creacion  = fecha_creacion  
        self.fecha_ult_modif  = fecha_ult_modif
        self.vigente = vigente

    def __repr__(self):
        return "Chistes Object (Id='%s')" % self.id

class chistes_schema(Schema):
    id = fields.Integer()
    descripcion = fields.String(required = True)
    vigente = fields.Boolean(missing=True)

    @post_load
    def make_chistes(self, data, **kwargs):
        return Chistes(**data)