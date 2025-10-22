from utilities.utils import get_rabbitmq_connection

class BaseWorker:
    def __init__(self, queue_name, config):
        self.queue_name = queue_name
        self.config = config

    def start(self):
        connection, channel = get_rabbitmq_connection(self.config)
        channel.queue_declare(queue=self.queue_name, durable=True)
        channel.basic_consume(
            queue=self.queue_name,
            on_message_callback=self.on_message,
            auto_ack=True
        )
        print(f"[{self.queue_name}] Worker started. Waiting for messages...")
        channel.start_consuming()

    def on_message(self, ch, method, properties, body):
        """
        Override in subclass with MRO feature.
        But it act as template if any worker class
        does not have on_message method.
        """
        print(f"[{self.queue_name}] Received: {body}")

