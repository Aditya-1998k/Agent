from base_worker import BaseWorker

class WelcomeWorker(BaseWorker):
    def on_message(self, ch, method, properties, body):
        print(f"[WelcomeWorker] New message: {body.decode()}")

