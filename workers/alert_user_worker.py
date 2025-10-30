from soa.base_worker import BaseWorker


class AlertUserWorker(BaseWorker):
    def on_message(self, ch, method, properties, body):
        print("Recieved message from alert user Queue.")

