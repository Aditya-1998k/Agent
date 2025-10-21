import pika
import configparser

def load_config(path="config.ini"):
    config = configparser.ConfigParser()
    config.read(path)
    return config

def get_rabbitmq_connection(config):
    creds = pika.PlainCredentials(
        config["RABBITMQ"]["username"],
        config["RABBITMQ"]["password"]
    )
    params = pika.ConnectionParameters(
        host=config["RABBITMQ"]["host"],
        port=int(config["RABBITMQ"]["port"]),
        virtual_host=config["RABBITMQ"]["virtual_host"],
        credentials=creds
    )
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    return connection, channel

