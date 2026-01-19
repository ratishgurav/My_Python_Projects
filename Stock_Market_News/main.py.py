import requests
from twilio.rest import Client
import os
from twilio.http.http_client import TwilioHttpClient
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
FUNC="TIME_SERIES_DAILY"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_price_api_key=os.environ.get("STOCK_APIKEY")
stock_price_param={
    "function":FUNC,
    "symbol":STOCK,
    "outputsize":"compact",
    "apikey":stock_price_api_key
}
response1=requests.get(url="https://www.alphavantage.co/query", params=stock_price_param)
data=response1.json()
prices=data["Time Series (Daily)"]
data_price=list(data["Time Series (Daily)"])
latest=data_price[0]
day_before_latest=data_price[1]
price_today=prices[latest]
price_before_today=prices[day_before_latest]

new_price=price_today["4. close"]
old_price=price_before_today["4. close"]
percentage=abs(round(((new_price-old_price)/old_price)*100,2))

## STEP 2: Use https://newsdata.io
# Instead of printing ("Get News"), actually get the first 3 news_data pieces for the COMPANY_NAME.

news_api_key= os.environ.get("NEWS_APIKEY")
news_params={
    "q": COMPANY_NAME,
    "apiKey":news_api_key,
    "language":"en"
}
response2=requests.get(url="https://newsapi.org/v2/everything",params=news_params)
news_data=response2.json()["articles"]

if old_price>new_price:
    news = (f'{STOCK} 🔻 {percentage} \n'
            f'{news_data[0]['author']}:{news_data[0]['title']}'
            f'\n{news_data[0]['description']}.')
else:
    news = (f'{STOCK} 🔺 {percentage} \n'
            f'{news_data[0]['author']}:{news_data[0]['title']}'
            f'\n{news_data[0]['description']}.')

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
now=dt.now()
day=now.weekday()
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_TOKEN")
proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

if day!=5 or day!=6:
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
            .create(
            body=news,
            from_="+12173946698",
            to=os.environ.get("TO_PHONE")
        )
    print(message.status)

#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

