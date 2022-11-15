class actividad(object):
    def __init__(self,id=None, descripcion=None, parent_id=None,fecha_creacion =None,creado_por =None,
                    fecha_modificacion =None,modificado_por =None,vigente=None):
        self.id = id
        self.descripcion = descripcion
        self.parent_id = parent_id
        self.fecha_creacion  = fecha_creacion 
        self.creado_por  = creado_por 
        self.fecha_modificacion  = fecha_modificacion 
        self.modificado_por  = modificado_por 
        self.vigente = vigente

    def __repr__(self):
        return "actividad Object (Id='%s')" % self.id
