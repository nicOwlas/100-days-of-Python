import json
import os
import smtplib
from datetime import date, timedelta

import requests
from dotenv import load_dotenv
from newsapi import NewsApiClient

load_dotenv()

STOCK_API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

## STEP 1: Use https://www.alphavantage.co
def is_changing(stock: str, trigger_value: float) -> bool:
    """When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News")."""
    parameters = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": stock,
        "apikey": STOCK_API_KEY,
    }
    response = requests.get(
        url="https://www.alphavantage.co/query", params=parameters, timeout=30
    )
    stock_history = response.json()["Time Series (Daily)"]

    yesterday = date.today() - timedelta(days=1)
    two_days_ago = date.today() - timedelta(days=2)

    yesterday_close_value = float(stock_history[f"{yesterday}"]["4. close"])
    two_days_ago_close_value = float(stock_history[f"{two_days_ago}"]["4. close"])
    relative_evolution = (
        abs(yesterday_close_value - two_days_ago_close_value) / yesterday_close_value
    )
    if relative_evolution > trigger_value:
        print(
            f"Stock is changing rapidly. Change: {relative_evolution:0.2%}. Fetching news"
        )
        return True


## STEP 2: Use https://newsapi.org
def get_news(search_string: str):
    """Get the first 3 news pieces for the COMPANY_NAME."""
    # Init
    newsapi = NewsApiClient(api_key=NEWS_API_KEY)

    # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(
        q=search_string,
        category="business",
        language="en",
        country="us",
    )

    return top_headlines


## STEP 3: Use https://www.twilio.com
def send_email(recipient_email: str, subject: str, message: str) -> None:
    """Send a seperate email with the percentage change and each article's title and description"""

    smtp_address = os.environ.get("SMTP_ADDRESS")
    email_sender = os.environ.get("EMAIL_SENDER")
    password_app = os.environ.get("PASSWORD_APP")

    with smtplib.SMTP(smtp_address) as connection:
        connection.starttls()
        connection.login(user=email_sender, password=password_app)
        connection.sendmail(
            from_addr=email_sender,
            to_addrs=recipient_email,
            msg=f"Subject:{subject}\n\n{message}",
        )


if __name__ == "__main__":
    email_recipient = os.environ.get("EMAIL_RECIPIENT")
    STOCK = "TSLA"
    COMPANY_NAME = "Tesla Inc"
    if is_changing(stock=STOCK, trigger_value=0.04):
        top_3_articles = get_news(search_string=COMPANY_NAME)["articles"][:3]
        print(top_3_articles)
        for article in top_3_articles:
            send_email(
                recipient_email=email_recipient,
                subject=f"Headline: {article.get('title')}",
                message=f"Brief: {article.get('description')}",
            )
