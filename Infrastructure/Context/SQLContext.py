class SQLContext(object):
    
    context_chistes_repository = None

    def __init__(self, app, band=True):
        from flask_sqlalchemy import SQLAlchemy
        from Infrastructure.Mapping import Mappings
        from Infrastructure.Repositories.ChistesRepository import ChistesRepository

        db = SQLAlchemy(app)
        if band:
            Mappings.init(db)

        self.db = db
        
        self.context_chistes_repository = ChistesRepository(db)
    
    def setup(self):
        self.db.create_all()
