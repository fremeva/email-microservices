import json

from celery import Celery
from kombu import Exchange, Queue

from data import ERRORS

from serveremail import send_email

app = Celery('reto1', broker='amqp://localhost', backend='amqp://guest:guest@localhost')

exch = Exchange('logs', 'fanout')
queue1 = Queue('q1', exclusive=True, exchange=exch)
queue2 = Queue('q2', exclusive=True, exchange=exch)

app.conf.task_queues = (
    queue1,
    queue2
)


@app.task(queue='q2', exchange=exch)
def email_worker(data):
    print('[*] Message for worker email_worker')
    print(data)
    print(send_email('Error del Servidor !!ALERTA!!', data, ['fredylsvprueba@gmail.com']))
    # message = '[{}] "{}" {}'.format(data['type'], data['code'], data['body'])


@app.task(queue='q1', exchange=exch)
def file_worker(data):
    print('[*] Message for worker file_worker')
    print(data)
    with open('logs.txt', 'a') as file:
        file.write('{}\n'.format(data))
    #     message = '[{}] "{}" {}'.format(data['type'], data['code'], data['body'])


@app.task()
def pub():
    return 'hello word'
    # return json.dumps({'type': 'DEBUG', 'code': '123', 'body': 'Error de debug'})


if __name__ == '__main__':
    pub.apply_async((), {}, exchange=exch, exchange_type='fanout', durable=True)
