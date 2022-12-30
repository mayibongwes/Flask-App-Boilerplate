import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "dbname"
database_path = "postgresql://{}:{}@{}/{}".format("username", "password", "localhost:5432", database_name)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

'''
MyDBModel

'''
class MyDBModel(db.Model):  
  __tablename__ = 'mydbmodel'

  id   = Column(Integer, primary_key=True)
  col1 = Column(String)
  col2 = Column(String)


  def __init__(self, col1, col2):
    self.col1 = col1
    self.col2 = col2

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self): 
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'col1': self.col1,
      'col2': self.col2
    }