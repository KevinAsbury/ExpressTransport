from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy import Column, Integer, String, create_engine
import json

database_filename = "expresstransport.sqlite3"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))

db = SQLAlchemy()

def setup_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

def db_drop_and_create_all():
    db.drop_all()
    db.create_all()

'''
Vehicle
A vehicle used for transport
'''
class Vehicle(db.Model):
    __tablename__ = 'Vehicles'
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    year = Column(Integer)
    make = Column(String)
    model = Column(String)
    VIN = Column(String)
    vtype = Column(String)

    def __init__(self, year, make, model, VIN, vtype):
        self.year = year
        self.make = make
        self.model = model
        self.VIN = VIN
        self.vtype = vtype
    
    def format(self):
        return {
            'id': self.id,
            'year': self.year,
            'make': self.make,
            'model': self.model,
            'VIN': self.VIN,
            'vtype': self.vtype
        }
    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
'''
Driver
Driver of a vehicle. 
'''
class Driver(db.Model):
    __tablename__ = 'Drivers'
    id = Column(Integer, primary_key=True)
    fname = Column(String)
    lname = Column(String)
    vtypes = Column(String)

    def __init__(self, fname, lname, vtypes):
        self.fname = fname
        self.lname = lname
        self.vtypes = vtypes

    def format(self):
        return {
            'id': self.id,
            'fname': self.fname,
            'lname': self.lname,
            'vtypes': self.vtypes
        }
    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()