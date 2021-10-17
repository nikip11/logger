import os, time
import helpers
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
import pika

# app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://mongodb:27017/myDatabase"
mongo = PyMongo(app)

credentials = pika.PlainCredentials('basic', 'qwerty12345')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    'rabbitmq',
    5672,
    '/',
    credentials
))
channel = connection.channel()

# @app.route('/logs')
# def get_all():
#     logs = mongo.db.logs.find()
#     return jsonify({'message': 'publisher working!!!', 'data': helpers.toJson(logs)})

# @app.route('/logs/<name>', methods=['GET'])
# def get_one(name):
#     find = {'name': name }
#     log = mongo.db.logs.find_one(find)
#     return jsonify({'message': 'publisher working!!!', 'data': helpers.toJson(log)})

# @app.route('/logs', methods=['POST'])
# def add_one():
#     log = request.json
#     log_id = mongo.db.logs.save(log)
#     log = mongo.db.logs.find_one({'_id': log_id})
#     return jsonify({'status': 'publisher working!!!', 'data': helpers.toJson(log)})


# def callback(ch, method, properties, body):
#     print(" [x] %r" % body)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    log = {'name': body.decode()}
    mongo.db.logs.save(log)
    ch.basic_ack(delivery_tag=method.delivery_tag)


# ========================================================================

# channel.exchange_declare(exchange='logs', exchange_type='fanout')

# result = channel.queue_declare(queue='', exclusive=True)
# queue_name = result.method.queue

# channel.queue_bind(exchange='logs', queue=queue_name)


# print(' [*] Waiting for logs. To exit press CTRL+C')

# channel.basic_consume(
#     queue=queue_name, on_message_callback=callback, auto_ack=True)

# channel.start_consuming()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('VIRTUAL_PORT'))
    channel.queue_declare(queue='logs', durable=True)
    print(' [*] Waiting for messages. To exit press CTRL+C ===')
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='logs', on_message_callback=callback)
    channel.start_consuming()
