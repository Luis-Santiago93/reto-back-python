class SQLContext(object):
    
    context_chistes_repository = None
    context_matematica_repository = None

    def __init__(self, app, band=True):
        from flask_sqlalchemy import SQLAlchemy
        from Infrastructure.Mapping import Mappings
        from Infrastructure.Repositories.ChistesRepository import ChistesRepository
        from Infrastructure.Repositories.MatematicoRepository import MatematicoRepository
        
        db = SQLAlchemy(app)
        if band:
            Mappings.init(db)

        self.db = db

        self.context_chistes_repository = ChistesRepository(db)
        self.context_matematica_repository = MatematicoRepository(app)

    def setup(self):
        self.db.create_all()
