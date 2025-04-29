import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()

class EmailService:
    def __init__(self, sender_email: str):
        self.sender_email = sender_email
        self.app_password = os.getenv('EMAIL_APP_PASSWORD')
        self.smtp_server = "smtp.gmail.com"
        self.port = 587 

    def send_email(self, to_email: str, subject: str, body: str):
        try:
            # Create the email
           
            message = MIMEMultipart()
            message["From"] = self.sender_email
            message["To"] = to_email
            message["Subject"] = subject

            message.attach(MIMEText(body, "plain"))

            # Connect to server and send
            server = smtplib.SMTP(self.smtp_server, self.port)
            server.starttls()
            server.login(self.sender_email, self.app_password)
            server.sendmail(self.sender_email, to_email, message.as_string())
            server.quit()

            print(f"Email sent to {to_email} ✅")
            return True
        except Exception as e:
            print(f"Failed to send email ❌: {e}")
            return False
