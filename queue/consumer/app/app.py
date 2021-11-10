import os
from ast import literal_eval
import pika
from pymongo import MongoClient

client = MongoClient(os.environ.get('MONGODB_URL'))
db = client.logger

credentials = pika.PlainCredentials(os.environ.get(
    'RABBITMQ_USER'), os.environ.get('RABBITMQ_PASSWORD'))
connection = pika.BlockingConnection(pika.ConnectionParameters(
    'rabbitmq',
    5672,
    '/',
    credentials
))
channel = connection.channel()


def callback(ch, method, properties, body):
    log = literal_eval(body.decode())
    print(log)
    db.logs.save(log)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.queue_declare(queue='logs', durable=True)

print(' [*] Waiting for messages. To exit press CTRL+C ===')
channel.basic_consume(queue='logs', on_message_callback=callback)
channel.start_consuming()
