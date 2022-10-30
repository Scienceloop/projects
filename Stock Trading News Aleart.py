import requests
from twilio.rest import Client
import os


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
FUNCTION = "TIME_SERIES_DAILY"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_api = os.environ('NEWS_API')
stock_api =os.environ('STOCK_API')
account_sid = os.environ('TWILIO_ACCOUNT_SID')
auth_token = os.environ('TWILIO_AUTH_TOKEN')

stock_parameters = {
    "function": FUNCTION,
    "symbol": STOCK,
    "apikey": stock_api
}

news_parameters = {
    "q": STOCK,
    "apiKey": news_api

}

response_stock = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response_stock.raise_for_status()
data = response_stock.json()["Time Series (Daily)"]

data_list =[value for (key, value) in data.items()]

yesterday_closing_price = float(data_list[0]["4. close"])
before_yesterday_closing_price = float(data_list[1]["4. close"])

difference = abs(yesterday_closing_price - before_yesterday_closing_price)

difference_percent = (difference/before_yesterday_closing_price)*100

if difference_percent >= 1:
    response_news = requests.get(NEWS_ENDPOINT, params=news_parameters)
    response_news.raise_for_status()
    data_news = response_news.json()["articles"][slice(3)]

    for i in range(3):
        news_title = data_news[i]['title']
        news_description = data_news[i]['description']
        news = f"{i + 1}. {news_title}: \n {news_description}"
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=news,
            from_='+11234567890',
            to='+911234567890'
        )
        print(message.status)
