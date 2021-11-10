import os
import helpers
from flask import Flask, json, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = os.environ.get('MONGODB_URL') + "logger"
mongo = PyMongo(app)


@app.route('/')
def welcome():
    return jsonify({'message': 'api working'})


@app.route('/logs')
def get_all():
    logs = mongo.db.logs.find()
    return jsonify({'message': 'publisher working!!!', 'data': helpers.toJson(logs)})


@app.route('/logs/', methods=['POST'])
def get_one():
    filter = request.json
    log = mongo.db.logs.find(filter)
    return jsonify({'message': 'publisher working!!!', 'data': helpers.toJson(log)})


@app.route('/logs', methods=['POST'])
def add_one():
    log = request.json
    log_id = mongo.db.logs.save(log)
    log = mongo.db.logs.find_one({'_id': log_id})
    return jsonify({'status': 'publisher working!!!', 'data': helpers.toJson(log)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('VIRTUAL_PORT'))
