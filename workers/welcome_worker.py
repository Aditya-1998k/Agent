import textwrap
from soa.base_worker import BaseWorker
from processor.send_mail import send_email

class WelcomeWorker(BaseWorker):
    def on_message(self, ch, method, properties, body):
        email = body.decode().strip()
        print(f"[WelcomeWorker] New message: {email}")
        subject = "Welcome to Task Tracker!"
        message = (
            """
            Dear Customer,

            Welcome to Task Tracker! We're excited to have you join our community.
            With Task Tracker, managing your tasks has never been easier.
            If you have any questions or need assistance, our support team is always here to help.

            Best regards,
            The Task Tracker Team
            """
        )
        message = textwrap.dedent(message)
        send_email(email, subject, message)

