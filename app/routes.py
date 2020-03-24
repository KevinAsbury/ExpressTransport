from app import app
from app.models import setup_db, db_drop_and_create_all, Delivery, Driver
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
    return jsonify('Hello World!')

@app.route('/deliveries', methods=['GET'])
@requires_auth('get:deliveries')
def get_deliveries(jwt):
    query = Delivery.query.all()
    deliveries = [q.format() for q in query]
    return jsonify(deliveries)

@app.route('/deliveries', methods=['POST'])
@requires_auth('post:deliveries')
def post_deliveries(jwt):
    req = request.get_json()
    description = req['description']
    new_delivery = Delivery(description)
    new_delivery.insert()
    return jsonify(new_delivery.format())

@app.route('/deliveries/<int:id>', methods=['PATCH'])
@requires_auth('patch:deliveries')
def update_deliveries(jwt, id):
    query = Delivery.query.get(id)
    req = request.get_json()
    if 'description' in req:
        query.description = req.get('description', '')
    if 'delivered' in req:
        query.delivered = req.get('delivered', None)
    if 'driver' in req:
        query.driver_id = req.get('driver', 0)
    query.update()
    return jsonify(query.format())

@app.route('/deliveries/<int:id>', methods=['DELETE'])
@requires_auth('delete:deliveries')
def delete_deliveries(jwt, id):
    query = Delivery.query.get(id)
    query.delete()
    return jsonify(query.format())

@app.route('/drivers', methods=['GET'])
@requires_auth('get:drivers')
def get_drivers(jwt):
    query = Driver.query.all()
    drivers = [q.format() for q in query]
    return jsonify(drivers)


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