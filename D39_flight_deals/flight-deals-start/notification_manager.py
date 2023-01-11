"""Send a notifications"""
import asyncio
import os
import smtplib

import aiosmtplib


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""

    def __init__(self) -> None:
        pass

    def format_email(self, flight: dict) -> dict:
        """Returns the subject and message for the email to be sent"""
        local_departure_date = flight.get("route")[0].get("local_departure")
        local_return_date = flight.get("route")[-1].get("local_arrival")
        email_subject = f"Found a cheaper ticket to {flight.get('cityTo')}".encode(
            "utf-8"
        )
        email_message = f"Destination: {flight.get('cityTo')}\n \
Price: {flight.get('price')}€\n \
Departure date: {local_departure_date}\n \
Return date: {local_return_date}\n".encode(
            "utf-8"
        )
        return {"subject": email_subject, "message": email_message}

    def send_email(self, *, recipient_email: str, subject: str, body: str) -> None:
        """Send an email"""

        smtp_address = os.environ.get("SMTP_ADDRESS")
        sender = os.environ.get("EMAIL_SENDER")
        password = os.environ.get("PASSWORD_APP")

        with smtplib.SMTP(smtp_address) as connection:
            connection.starttls()
            connection.login(user=sender, password=password)
            connection.sendmail(
                from_addr=sender,
                to_addrs=recipient_email,
                msg=f"Subject:{subject}\n\n{body}",
            )

    async def send_async_email(
        self, *, recipient_email: str, subject: str, body: str
    ) -> None:
        """Send an email in async"""
        smtp_address = os.environ.get("SMTP_ADDRESS")
        sender = os.environ.get("EMAIL_SENDER")
        password = os.environ.get("PASSWORD_APP")
        smtp = aiosmtplib.SMTP(hostname=smtp_address, use_tls=True)
        await smtp.connect()
        await smtp.login(username=sender, password=password)
        await smtp.sendmail(
            sender=sender,
            recipients=recipient_email,
            message=f"Subject:{subject}\n{body}",
        )
        await smtp.quit()


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    EMAIL_TO = os.environ.get("EMAIL_RECIPIENT")
    notification_manager = NotificationManager()

    async def main():
        """Sync and async emails"""
        notification_manager.send_email(
            recipient_email=EMAIL_TO, subject="Hello Nico", body="Test message"
        )

        await notification_manager.send_async_email(
            recipient_email=EMAIL_TO,
            subject="Hello Nico Async",
            body="Test async message",
        )

    asyncio.run(main())
