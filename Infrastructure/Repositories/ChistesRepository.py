
import requests
from settings import create_app, ENVIRONMENT_NAME
from Infrastructure.Repositories.Complements.Utils import *
from Infrastructure.Repositories.RepositoryBase import RepositoryBase
from Infrastructure.Entities.Core.Chistes import Chistes

app = create_app(ENVIRONMENT_NAME)


WEAPI_CHUCKNORRIS = app.config["WEAPI_CHUCKNORRIS"]
WEAPI_JOKE = app.config["WEAPI_JOKE"]
VERIFY_SSL = app.config["VERIFY_SSL"]


def get_json(i, name):
    if name == 'chuck':
        return {
        'id': i['id'],
        'value' : i['value']
        }
    elif name == 'joke':
        return {
        'id': i['id'],
        'value' : i['joke']
        }


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
            query = self.session().query(Chistes).all()
            for i in query:
                
                print(i.id)
            
            row = get_json(re, name = 'chuck')
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

            row = get_json(re, name = 'joke')
            return row
        except Exception as e:
            print(e)
            return None
        
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

    def update(self, item,id):
        super().update(serialize(item),id)
        return True