import os
import smtplib
import random
import datetime as dt
import pandas
from dotenv import load_dotenv
load_dotenv()

def is_birthday_today(friends_dataframe):
    """Add a column with 0s and 1s for the records having a birthday today"""

    today = dt.date.today()
    friends_dataframe = friends_dataframe.assign(is_birthday_today=0)
    for index, birthday in friends_dataframe.iterrows():
        birth_month = birthday.month
        birth_day = birthday.day

        if today == dt.date(year=today.year, month=birth_month, day=birth_day):
            friends_dataframe.at[index,"is_birthday_today"] = 1
    return friends_dataframe

def send_email(email_recipient,email_message):
    """Sends an email. The sender email is defined in the .env file"""

    smtp_address = os.environ.get("SMTP_ADDRESS")
    email_sender = os.environ.get("EMAIL_SENDER")
    password_app = os.environ.get("PASSWORD_APP")

    with smtplib.SMTP(smtp_address) as connection:
        connection.starttls()
        connection.login(user=email_sender, password=password_app)
        connection.sendmail(from_addr=email_sender,
        to_addrs=email_recipient,
        msg=f"Subject:Happy Birthday!\n\n{email_message}")

# Load the CSV file
friends = pandas.read_csv("./birthdays.csv")

# Add a column with 1s for friends having birthday today
friends = is_birthday_today(friends)

# Filter the dataframe to the happy few having birthday today
friends_having_birthday = friends[friends["is_birthday_today"] == 1]

# For the friends with birthday, send them an email
for _, friend in friends_having_birthday.iterrows():
    letter_index = random.randint(1,3)
    with open(f"./letter_templates/letter_{letter_index}.txt", encoding="UTF-8") as file:
        generic_message = file.read()
    message = generic_message.replace("[NAME]",friend["name"])
    # send_email(email_recipient=friend["email"], email_message=message)
