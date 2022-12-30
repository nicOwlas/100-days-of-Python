import datetime as dt
from random import choice
from dotenv import load_dotenv
import os
import smtplib
load_dotenv()

# Trigger when today is a Monday
weekday = dt.datetime.now().weekday()

if weekday == 0:

    # Open quotes file
    with open(file="./quotes.txt", encoding="UTF-8") as file:
        quotes = file.readlines()

    quote_of_the_day = choice(quotes)

    # Send EMAIL
    smtp_address = os.environ.get("SMTP_ADDRESS")
    email_sender = os.environ.get("EMAIL_SENDER")
    email_recipient = os.environ.get("EMAIL_RECIPIENT")
    password_app = os.environ.get("PASSWORD_APP")

    with smtplib.SMTP(smtp_address) as connection:
        connection.starttls()
        connection.login(user=email_sender, password=password_app)
        connection.sendmail(from_addr=email_sender,
        to_addrs=email_recipient,
        msg=f"Subject:Quote of the day\n\n{quote_of_the_day}")

else:
    print("Not today")