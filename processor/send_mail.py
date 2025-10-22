import smtplib
from email.mime.text import MIMEText
from utilities.utils import load_config


def send_email(to_email, message):
    """Send a welcome letter to user."""
    config = load_config()
    from_email = config['EMAIL']['from_email']
    password = config['EMAIL']['password']

    subject = "Welcome to Task Tracker!"

    msg = MIMEText(message, "plain")
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(from_email, password)
            server.send_message(msg)
        print(f"[WelcomeWorker] Email sent successfully to {to_email}")
    except Exception as e:
        print(f"[WelcomeWorker] Failed to send email to {to_email}: {e}")
