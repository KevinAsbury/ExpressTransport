from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from models import Driver, Vehicle, db_drop_and_create_all, setup_db

app = Flask(__name__)
CORS(app)
setup_db(app)

'''
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''
# db_drop_and_create_all()

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    return 'To be implemented'

@app.route('/vehicles', methods=['POST'])
def post_vehicle():
    return 'To be implemented'

@app.route('/vehiles/<int:id>', methods=['PATCH'])
def update_vehicle(id):
    return 'To be implemented'

@app.route('/vehicles/<int:id>', methods=['DELETE'])
def delete_vehicle(id):
    return 'To be implemented'

@app.route('/drivers', methods=['GET'])
def get_drivers():
    return 'To be implemented'

@app.route('/drivers', methods=['POST'])
def post_driver():
    return 'To be implemented'

@app.route('/drivers/<int:id>', methods=['PATCH'])
def update_driver(id):
    return 'To be implemented'

@app.route('/drivers/<int:id>', methods=['DELETE'])
def delete_driver(id):
    return 'To be implemented'