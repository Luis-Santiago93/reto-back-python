import flask_sqlalchemy
from sqlalchemy import ForeignKey, ForeignKeyConstraint,Integer, String, Boolean, DateTime, Float, Text, JSON, Date,Numeric,SMALLINT,BigInteger, and_
from sqlalchemy.dialects.mssql import BIT
from sqlalchemy.orm import mapper, relationship
from sqlalchemy.dialects import mysql
import datetime

from sqlalchemy.sql.sqltypes import DECIMAL, SmallInteger
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
