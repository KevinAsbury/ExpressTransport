# MyExpressWay

Heroku App: [MyExpressWay](https://myexpressway.herokuapp.com/)

My [Udacity](https://www.udacity.com/) Full Statck Developer Nanodegree program final project. The MyExpressWay app is used by an imaginary delivery company. They have drivers who need to login and mark if they are available and they have managers who need to login and see available drivers and deliveries. 

## Getting Started

### Create a Virutal Enviornment

Follow instructions on the [Pipenv site](https://pipenv-fork.readthedocs.io/en/latest/) to install and run pipenv.
Run 'pipenv shell' to create, install dependencies, and start the virtual environment.

### Install Postman

Follow instructions on the [Postman docs](https://www.getpostman.com/) to install and run postman.

### Run the Server

## Environment Variables
run `./setup.sh` to load the environment variables.

# Development:
Type `flask run --reload` to run the developer server.

# Production:
Type `gunicorn -b localhost:5000 -w 2 app:app` to run a production server.

## AUTH0 Permissions and Roles
There are two primary roles in the application: the manager and the driver. The manager can access all aspects of the deliveries while the driver need only see available deliveries and update deliveries to mark them delivered.

Manager Permissions:
-get:deliveries
-post:deliveries
-patch:deliveries
-delete:deliveries

Driver Permissions:
-get:deliveries
-patch:deliveries

### Endpoints

--------------------------
GET /

The application root.
--------------------------
GET /deliveries

Returns a json list of deliveries.

[
    {
        "delivered": false,
        "description": "Softest Wheat Bread",
        "driver_id": 1,
        "id": 1
    },
    {
        "delivered": false,
        "description": "2% Milk",
        "driver_id": null,
        "id": 2
    }
]
--------------------------
POST /deliveries

Create a new delivery. Returns a description of the posted item.

{
    "description": "Softest Potato Bread"
}
--------------------------
PATCH /deliveries/<id>

Update a delivery by the provided id. Returns the patched item.

{
    "description": "Softest Wheat Bread",
    "driver": 1,
    "delivered": false
}
--------------------------
DELETE /deliveries/<id>

Delete a delivery by the provided id. Returns a json representation of the deleted item.

{
    "delivered": false,
    "description": "Softest Potato Bread",
    "driver_id": null,
    "id": 6
}
--------------------------
GET /drivers

Get a list of drivers.

`[
    {
        "fname": "John",
        "id": 1,
        "lname": "Smith"
    },
    {
        "fname": "Karen",
        "id": 2,
        "lname": "Winters"
    }
]`
--------------------------