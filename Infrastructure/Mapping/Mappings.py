
from sqlalchemy import ForeignKey, Integer, String, Boolean, DateTime, Float, Text, JSON, Date,Numeric
from sqlalchemy.orm import mapper, relationship
import datetime

from Infrastructure.Entities.Core.Chistes import Chistes

def init(db):

    chistes_mapping = db.Table('chistes',
        db.Column('id', Integer, primary_key=True),  
        db.Column('descripcion', String(255)),
        db.Column('fecha_creacion',DateTime),
        db.Column('fecha_modificacion', DateTime),
        db.Column('vigente', Boolean)
    )

    db.mapper(Chistes, chistes_mapping)