from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# also import other db models
# from app.models import setup_db, MyDBModel

# get routes
from app.routes import main

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
#   setup_db(app)
  CORS(app)

  # CORS Headers
  @app.after_request
  def after_request(response):
      response.headers.add(
          "Access-Control-Allow-Origin", "*"
      )
      return response

  # add routes to the app
  app.register_blueprint(main)
  
  return app

    