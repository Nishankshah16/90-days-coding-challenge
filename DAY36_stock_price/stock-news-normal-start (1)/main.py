# https://www.tradingview.com/symbols/NASDAQ-TSLA/      -- stock price
import datetime as dt
import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

tiwilo_sid=""
twilio_auth=""
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
api_key=""

parameters={
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": api_key
}
url = STOCK_ENDPOINT


#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response=requests.get(url=url, params=parameters)
data=response.json()["Time Series (Daily)"]

lst = [value for (key, value) in data.items()]
yesterday_price=lst[0]["4. close"]
# day_before_yesterday_price= lst[1]["4. close"]

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_price= lst[1]["4. close"]
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp 
difference= abs(float(day_before_yesterday_price)-float(yesterday_price))

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
difference_percentage= (float(difference)/float(yesterday_price))*100
# print(difference_percentage)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
# api_news="c4305c13589d4cb993297abfaa7a4c0e"
news_parameters={
    "apiKey":"",
    "q":"Tesla",
    "searchIn":"title"
}
# if difference_percentage >5:
response_news=requests.get(url=NEWS_ENDPOINT,params=news_parameters)
news_data=response_news.json()["articles"]


    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
articles_3= news_data[:3]
# print(articles_3)
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.


#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
formated_articles=[f"Headline: {articles["title"]}. \nBrief:{articles["description"]} " for articles in articles_3]

#TODO 9. - Send each article as a separate message via Twilio. 
client = Client(tiwilo_sid, twilio_auth)
for article in formated_articles:
    message = client.messages.create(
    body="Tesla stock message", 
    from_= "",#TWILIO_NUMBER     # from_="whatsapp:TWILIO_WHATSAPP_NUMBER",   -- for whatspp msg
    to= "",#VERIFIED_NUMBER
    )
    print(message.status)


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

