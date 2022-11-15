from Infrastructure.Entities.Core.ActoIlicito import acto_ilicito
from Infrastructure.Repositories.RepositoryBase import RepositoryBase
from Infrastructure.Repositories.Complements.Utils import *

def get_json(i):
    return {
        'id': i.id,
        'actividad_id' : i.actividad_id,
        'actividad': i.actividad.descripcion if i.actividad_id is not None else None,
        'danio_equipo' : i.danio_equipo,
        'costo_produccion_diferida' :str(i.costo_produccion_diferida),
        'vigente': i.vigente
    }


class ActoIlicitoRepository(RepositoryBase):
    db = None

    def __init__(self, db):
        self.db = db
        super().__init__(db, entity_base = acto_ilicito, entity_name='acto_ilicito')

    def get_by_id(self, id):
        try:
            query = self.session().query(acto_ilicito).filter_by(id=id).first()
            if query is None:
                return None
            i = get_json(query)
            return i
            self.session().commit()
        except Exception as e:
            print(e)
            raise e
            self.session().rollback()
            raise
        finally:
            self.session().close()
    
    def get_by_evento(self, id):
        try:
            query = self.session().query(acto_ilicito).filter_by(evento_id=id).all()
            if not query:
                return None
            else:
                i = [get_json(i) for i in query]
                return i
            self.session().commit()
        except Exception as e:
            print(e)
            raise e
            self.session().rollback()
            raise
        finally:
            self.session().close()

    def get_all(self):
        return [get_json(i) for i in super().get_all()]
    
    def insert(self, item):
        try:
            self.session().add(item)
            self.session().commit()
            self.session().refresh(item)
            return get_json(item)
        except Exception as e:
            return None
           

    def update(self, item,id):
        super().update(serialize(item),id)
        return True

    def disabled(self, id):
        super().disabled(id)
        return True
