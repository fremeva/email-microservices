import json
import time

from connection import PikaConnection


def errors():
    return [
        {'type': 'DEBUG', 'code': '123', 'body': 'Error de debug'},
        {'type': 'WARRNING', 'code': '234', 'body': 'Error de debug'},
        {'type': 'INFO', 'code': '200', 'body': 'Error de debug'},
        {'type': 'INFO', 'code': '200', 'body': 'Nueva Informacion'},
        {'type': 'ERROR', 'code': '500', 'body': 'Ha ocurrido un error en el servidor .......'},
        {'type': 'ERROR', 'code': '500', 'body': 'Ha ocurrido un 2° error en el servidor .......'},
        {'type': 'DEBUG', 'code': '123', 'body': 'Error de debug'},
    ]


if __name__ == '__main__':
    connection = PikaConnection()
    connection.channel.exchange_declare(exchange='logs', exchange_type='direct')

    for error in errors():
        message = json.dumps(error)
        connection.channel.basic_publish(
            exchange='logs',
            routing_key=error['type'],
            body=message
        )
        print("[*] Sent message : {}".format(message))
        time.sleep(3)

    # Close Connection
    connection.close()
