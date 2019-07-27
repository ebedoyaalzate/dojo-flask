from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo
from flask_cors import CORS
from api.controller.car import Car
from api.controller.car import CarList


app = Flask(__name__)

app.config['MONGO_URI'] = ''

app.database = PyMongo(app)

app.cars_collection = app.database.db.cars

# Configure CORS
cors = CORS(app,  origins=['http://mongodb://3.14.7.212:27017/Cars:8080'])

#Create api

api = Api(app)

api.add_resource(Car, '/car', '/car/<car_id>',
                 methods=['GET', 'POST', 'PUT', 'DELETE'])

api.add_resource(CarList, '/cars',
                 methods=['GET'])
