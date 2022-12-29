import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
smtp_address = os.environ.get("SMTP_ADDRESS")
email_sender = os.environ.get("EMAIL_SENDER")
email_recipient = os.environ.get("EMAIL_RECIPIENT")
password_app = os.environ.get("PASSWORD_APP")

with smtplib.SMTP(smtp_address) as connection:
    connection.starttls()
    connection.login(user=email_sender, password=password_app)
    connection.sendmail(from_addr=email_sender,
    to_addrs=email_recipient,
    msg="Subject:Hello\n\nBlabliblu")