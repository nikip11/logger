import os, sys
from datetime import datetime, timezone
from flask import Flask, jsonify, request
import pika

app = Flask(__name__)

credentials = pika.PlainCredentials(os.environ.get('RABBITMQ_USER'), os.environ.get('RABBITMQ_PASSWORD'))
parameters = pika.ConnectionParameters(
                'rabbitmq',
                5672,
                '/',
                credentials
            )

def getChannel():
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue='logs', durable=True)
    return channel

@app.route('/')
def welcome():
    return jsonify({'status': 'consumer working!!!!!'})

@app.route('/logs', methods=['POST'])
def rabbit():
    channel = getChannel()
    message=request.json
    message['created_at'] = datetime.utcnow().isoformat()
    print(message)
    message = str(message)
    channel.basic_publish(
        exchange='',
        routing_key='logs',
        body=message)
    return jsonify({'status': 'log sended'})

# @app.route('/logs/test-send')
# def test_rabbit2():
#     # message = ' '.join(sys.argv[1:]) or "Hello World!"
    # message=str({
    #     "name": "prueba7",
    #     "enviroment": "dev",
    #     "url": "https://np11.es",
    #     "user": "guest",
    #     "browser": "brave",
    #     "ip": "localhost",
    #     "meta": {}
    # })
#     channel.basic_publish(
#         exchange='',
#         routing_key='logs',
#         body=message)
#     print(" [x] Sent %r" % message)
#     # connection.close()
#     return jsonify({'status': 'rabbit consumer working'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('VIRTUAL_PORT'))

