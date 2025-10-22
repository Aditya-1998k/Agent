import textwrap
import json
from soa.base_worker import BaseWorker
from processor.send_mail import send_email

class MLWorker(BaseWorker):
    def on_message(self, ch, method, properties, body):
        data = json.loads(body.decode())
        email = data.get("user_email")
        print(f"[ML QUEUE] New message: {email}")
        subject = "ML Model Prediction Summary!"
        summary = f"""
        Hello,

        Here’s your Better Life Index (BLI) summary for {data['country']}:

        - BLI based on global data (linear regression model): {data['better_life_index with with Global data (linear regression_model)']}
        - BLI compared to 3 nearest neighbors (k-means cluster model): {data['better_life_index wrt 3 nearest neibour (kmeans cluster model)']}
        - Overall comparison: {data['comparison']}

        Best regards,
        The Better Life Index Team
        """
        message = textwrap.dedent(summary)
        send_email(email, subject, message)
