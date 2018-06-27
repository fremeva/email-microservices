import pika
import json


def pub_send_email(data):
    with pika.BlockingConnection(pika.ConnectionParameters('localhost')) as connection:
        channel = connection.channel()
        channel.queue_declare(queue="emails")
        channel.basic_publish(
            exchange="",
            routing_key="emails",
            body=data
        )


if __name__ == '__main__':
    subj = input('subject: ')
    to = input('to (separated by ","): ')
    body = input('body: ')

    data = {'subject': subj, 'to': to.split(','), 'body': body}
    pub_send_email(json.dumps(data))
