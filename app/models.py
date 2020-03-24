from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey #, create_engine
from sqlalchemy.orm import relationship
import json

database_filename = "myexpressway.sqlite3"
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
Delivery
A product available for delivery
'''
class Delivery(db.Model):
    __tablename__ = 'deliveries'
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    description = Column(String)
    delivered = Column(Boolean)
    driver_id = Column(Integer, ForeignKey('drivers.id'))
    driver = relationship("Driver", back_populates="deliveries")

    def __init__(self, description):
        self.description = description
        self.delivered = False
    
    def format(self):
        return {
            'id': self.id,
            'description': self.description,
            'delivered': self.delivered,
            'driver_id': self.driver_id
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
    __tablename__ = 'drivers'
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    fname = Column(String)
    lname = Column(String)
    deliveries = relationship("Delivery", back_populates="drivers")

    def __init__(self, fname, lname, vehicle):
        self.fname = fname
        self.lname = lname

    def format(self):
        return {
            'id': self.id,
            'fname': self.fname,
            'lname': self.lname,
        }
    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()