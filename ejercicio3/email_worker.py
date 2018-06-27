import json

from connection import PikaConnection

from server_email import send_email


def callback(ch, method, properties, body):
    data = json.loads(str(body)[2:-1:])
    if data['type'] == 'ERROR':
        print('[*] Message for broker {} : {}'.format(queue_name, body))
        message = '[{}] "{}" {}'.format(data['type'], data['code'], data['body'])
        print(send_email('Error del Servidor !!ALERTA!!', message, ['fredylsvprueba@gmail.com']))


if __name__ == '__main__':
    connection = PikaConnection()
    channel = connection.channel

    channel.exchange_declare(exchange='logs', exchange_type='direct')

    results = channel.queue_declare(exclusive=True)
    queue_name = results.method.queue
    channel.queue_bind(exchange='logs', queue=queue_name, routing_key='ERROR')

    print('[*] Starting worker with queue {}'.format(queue_name))

    channel.basic_consume(callback, queue=queue_name, no_ack=True)
    channel.start_consuming()
