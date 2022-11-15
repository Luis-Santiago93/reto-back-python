from Infrastructure.Entities.Core.Chistes import Chistes, chistes_schema
from Infrastructure.Repositories.RepositoryBase import RepositoryBase
from Infrastructure.Repositories.Complements.Utils import *
from sqlalchemy import func
import datetime
import logging
import requests
from settings import create_app, ENVIRONMENT_NAME

app = create_app(ENVIRONMENT_NAME)

WEAPI_CHUCKNORRIS = app.config["WEAPI_CHUCKNORRIS"]
WEAPI_JOKE = app.config["WEAPI_JOKE"]
VERIFY_SSL = app.config["VERIFY_SSL"]


def get_info(i, name):
    if name == 'chuck':
        return {
        'id': i['id'],
        'descripcion' : i['value']
        }
    elif name == 'joke':
        return {
        'id': i['id'],
        'descripcion' : i['joke']
        }
        
def get_json(i,type_dict):
    
    summary_schema=chistes_schema(many=type_dict,only=(
        "id",
        "descripcion"
        )
    )
    
    return summary_schema.dump(i)

class ChistesRepository(RepositoryBase):
    db = None

    def __init__(self, db):
        self.db = db
        super().__init__(db, entity_base=Chistes, entity_name='Chistes')

    def get_api_chucknorris(self):
        try:
            url = WEAPI_CHUCKNORRIS + f'/random'
            headers = {'content-type': 'application/json'}
            
            r = requests.get(url, headers=headers, verify=VERIFY_SSL)
            if r.status_code not in (200, 201):
                return None
            re = r.json()          
            row = get_info(re, name = 'chuck')
            return row
        except Exception as e:
            print(e)
            return None
        
    def get_api_joke(self):
        try:
            url = WEAPI_JOKE
            headers = {'Accept': 'application/json'}
            
            r = requests.get(url, headers=headers, verify=VERIFY_SSL)
            if r.status_code not in (200, 201):
                return None
            re = r.json()

            row = get_info(re, name = 'joke')
            return row
        except Exception as e:
            print(e)
            return None
    
    def get_by_id(self, id):
        try:
            query = self.session().query(Chistes).filter_by(id=id,vigente=True).first()
            if query is None:
                return None
            i = get_json(query,False)
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
        try:
            query = self.session().query(Chistes).filter(Chistes.vigente == True).all()
            print(query)
            now = datetime.datetime.now()
            
            dt_string = now.date()
            print(now)
            logging.warning(str(now))
            logging.warning(str(now))
            return 'x'
        except Exception as e:
            return None
            self.session().rollback()
            raise
        finally:
            self.session().close()

    def get_by_element(self, id):
        try:
            return self.session().query(Chistes).filter_by(id=id, vigente=True).first()
        except Exception as e:
            raise e
        finally:
            self.session().close()

    def insert(self, item):
        try:
            self.session().add(item)
            self.session().commit()
            self.session().refresh(item)
            return get_json(item,False)
        except Exception as e:
            return None
            self.session().rollback()
            raise
        finally:
            self.session().close()

    def update(self, item):
        try:
            super().update(serialize(item),item.id)
            return True
        except Exception as e:
            print(e)
            self.session().rollback()
            raise
        finally:
            self.session().close()
        

    def disabled(self, id):
        try:
            self.session().query(self.entity_base).filter_by(id_lego_convivencia=id).update({'vigente': False})
            self.session().commit()
            return True
        except Exception as e:
            self.session().rollback()
            raise
        finally:
            self.session().close()
