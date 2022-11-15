from marshmallow import Schema, fields, missing, validate, post_load
from Domain.DomainServices.DomainBase import BaseSchema

class comision(object):
    def __init__(
        self,
        id_lego_comision = None,
        id_producto_comercial = None,
        version_producto = None,
        id_udm_comision = None,
        id_comision  = None,
        id_tipo_comision = None,
        id_udp_cobro_comision = None,
        periodo_cobro_comision = None,
        monto_comision = None,
        fecha_creacion = None,
        usuario_creacion = None,
        fecha_ult_modif = None,
        usuario_ult_modif = None,
        vigente = None,
        
    ):
        self.id_lego_comision = id_lego_comision
        self.id_producto_comercial =  id_producto_comercial
        self.version_producto =  version_producto
        self.id_udm_comision = id_udm_comision
        self.id_comision = id_comision
        self.id_tipo_comision = id_tipo_comision
        self.id_udp_cobro_comision= id_udp_cobro_comision
        self.monto_comision = monto_comision
        self.periodo_cobro_comision = periodo_cobro_comision
        #self.ind_registro_comision = ind_registro_comision
        self.fecha_creacion  = fecha_creacion 
        self.usuario_creacion  = usuario_creacion 
        self.fecha_ult_modif  = fecha_ult_modif 
        self.usuario_ult_modif  = usuario_ult_modif 
        self.vigente = vigente
        
    def __repr__(self):
        return "comision Object (Id='%s')" % self.id_lego_comision

class comision_ids_schema(Schema):
    id_lego_comision = fields.List(fields.Integer())
    
class comisionSchema(BaseSchema):
    id_lego_comision = fields.Integer()
    id_producto_comercial = fields.String(required = True)
    version_producto = fields.Integer(required = True)
    id_udm_comision = fields.Integer()
    id_comision = fields.Float()
    id_tipo_comision = fields.Integer()
    id_udp_cobro_comision = fields.Integer() 
    monto_comision = fields.Float() 
    periodo_cobro_comision = fields.Integer()
    #ind_registro_comision = fields.Boolean()
    vigente = fields.Boolean(missing=True)

    @post_load
    def make_comision(self, data, **kwargs):
        return comision(**data)
    
class comision_schema(BaseSchema):
    id_lego_comision = fields.Integer()
    id_producto_comercial = fields.String(required = True)
    version_producto = fields.Integer(required = True)
    id_udm_comision = fields.Integer()
    id_comision = fields.Float()
    id_tipo_comision = fields.Integer()
    id_udp_cobro_comision = fields.Integer(missing=None) 
    monto_comision = fields.Float() 
    periodo_cobro_comision = fields.Integer(missing=None)
    ind_registro_comision = fields.Boolean()
    vigente = fields.Boolean(missing=True)
