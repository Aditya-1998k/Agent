import textwrap
import json
from soa.base_worker import BaseWorker
from processor.send_mail import send_email

class UserPasswordWorker(BaseWorker):
    def on_message(self, ch, method, properties, body):
        data = json.loads(body.decode('utf-8'))
        email = data.get("email")
        password = data.get("password")
        print(f"[UserPasswordWorker] New message: {email}")
        subject = "Password Change!"
        message = (
            f"""
            Dear Customer,

            You have recieved request from you to change the password. Please
            make sure do not share this password with anyone.

            password: {password}

            Best regards,
            The Task Tracker Team
            """
        )
        message = textwrap.dedent(message)
        send_email(email, subject, message)
