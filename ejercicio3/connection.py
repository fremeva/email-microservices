import pika


class PikaConnection:

    def __init__(self, hostname='localhost'):
        self.__connection = pika.BlockingConnection(pika.ConnectionParameters(hostname))
        self.__chanel = self.__connection.channel()

    @property
    def channel(self):
        return self.__chanel

    def close(self):
        self.__connection.close()
        return True
