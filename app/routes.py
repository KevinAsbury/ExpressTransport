from app import app
from app.models import setup_db, db_drop_and_create_all
from flask import request, jsonify
from flask_cors import CORS
import json
from app.auth import requires_auth

CORS(app)
setup_db(app)

'''
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''
#db_drop_and_create_all()

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/deliveries', methods=['GET'])
@requires_auth('get:deliveries')
def get_vehicles():
    return 'To be implemented'

@app.route('/deliveries', methods=['POST'])
@requires_auth('post:deliveries')
def post_vehicle():
    return 'To be implemented'

@app.route('/deliveries/<int:id>', methods=['PATCH'])
@requires_auth('patch:deliveries')
def update_vehicle(id):
    return 'To be implemented'

@app.route('/deliveries/<int:id>', methods=['DELETE'])
@requires_auth('delete:deliveries')
def delete_vehicle(id):
    return 'To be implemented'

@app.route('/drivers', methods=['GET'])
@requires_auth('get:drivers')
def get_drivers():
    return 'To be implemented'

@app.route('/drivers', methods=['POST'])
@requires_auth('post:drivers')
def post_driver():
    return 'To be implemented'

@app.route('/drivers/<int:id>', methods=['PATCH'])
@requires_auth('patch:drivers')
def update_driver(id):
    return 'To be implemented'

@app.route('/drivers/<int:id>', methods=['DELETE'])
@requires_auth('delete:drivers')
def delete_driver(id):
    return 'To be implemented'


## Error Handling
@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
                    "success": False,
                    "error": 401,
                    "message": "unauthorized"
                    }), 401


@app.errorhandler(403)
def forbidden(error):
    return jsonify({
                    "success": False,
                    "error": 403,
                    "message": "forbidden"
                    }), 403


@app.errorhandler(404)
def not_found(error):
    return jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
                    "success": False, 
                    "error": 422,
                    "message": "unprocessable"
                    }), 422