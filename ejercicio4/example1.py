from celery import Celery
from server_email import send_email

app = Celery('example1', backend="amqp://guest:guest@localhost", broker="amqp://localhost")


@app.task
def worker(subject, to, body):
    print(send_email(subject, body, to))


def publisher():
    subj = input('subject: ')
    to = input('to (separated by ","): ')
    body = input('body: ')
    worker.delay(subj, to.split(','), body)


if __name__ == '__main__':
    publisher()
