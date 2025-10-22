from base_worker import BaseWorker
from processor.send_mail import send_email

class WelcomeWorker(BaseWorker):
    def on_message(self, ch, method, properties, body):
        email = body.decode().strip()
        print(f"[WelcomeWorker] New message: {email}")
        send_email(to_email=email)


