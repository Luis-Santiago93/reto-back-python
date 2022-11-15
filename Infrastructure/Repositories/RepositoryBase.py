import sqlalchemy
from sqlalchemy import update
from sqlalchemy import event

class RepositoryBase(object):
    entity_base = None
    entity_name = None

    def __init__(self, db, entity_base, entity_name):
        self.db = db
        self.entity_base = entity_base
        self.entity_name = entity_name
        
    def session(self):
        return self.db.session

    def get_all(self):
        try:
            return self.session().query(self.entity_base).all()
        except Exception as e:
            raise e
        finally:
            self.session().close()

    def get_by_element(self,id):
        try:
            return self.session().query(self.entity_base).get(id)
        except Exception as e:
            raise e
        finally:
            self.session().close()

    def insert(self, item):
        try:
            self.session().add(item)
            self.session().commit()
            self.session().refresh(item)
            return item
        except Exception as e:
            self.session().rollback()
            raise
        finally:
            self.session().close()

    def insert_all(self, items):
        try:
            result = []
            self.session().add_all(items)
            self.session().commit()
            for i in items:
                self.session().refresh(i)
                item = {}
                for key, value in i.__dict__.items():
                    if key != '_sa_instance_state':
                        item[key] = value
                result.append(item)
            return result
        except Exception as e:
            self.session().rollback()
            raise
        finally:
            self.session().close()

    def delete(self, id):
        try:
            i = self.session().query(self.entity_base).get(id)
            self.session().delete(i)
            self.session().commit()
        except Exception as e:
            self.session().rollback()
        finally:
            self.session().close()

    def update(self, item,id):
        try:
            i = self.session().query(self.entity_base).get(id)
            for key, value in sorted(item.items()):
                setattr(i, key, value)
            self.session().commit()
        except Exception as e:
            self.session().rollback()
            raise
        finally:
            self.session().close()

    def disabled(self,id):
        try:
            self.session().query(self.entity_base).filter_by(id=id).update({'vigente':False})
            self.session().commit()
        except Exception as e:
            self.session().rollback()
            raise
        finally:
            self.session().close()
