import json
import pika

from server_email import send_email

if __name__ == "__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue="emails")


    def emails(ch, method, properties, body):
        data = json.loads(str(body)[2:-1:])
        print(send_email(data['subject'], data['body'], data['to']))


    channel.basic_consume(emails, queue='emails', no_ack=True)
    print("Worker Initied!!!")
    channel.start_consuming()
