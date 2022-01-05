#temp email
#https://dropmail.me/en/

import yagmail
import pandas as pd
from news import NewsFeed
import datetime
import time


def send_email():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    news_feed = NewsFeed(interest=row['interest'],
                         from_date=yesterday,
                         to_date=today)
    email = yagmail.SMTP(user="email1@example.com", password="passwordhere")
    email.send(to=row['email'],
               subject=f"Your {row['interest']} news for today",
               contents=f"Hi {row['name']}\n See what's on about {row['interest']} today. \nUser \n\n{news_feed.get()}")


while True:
    if datetime.datetime.now().hour == 15 and datetime.datetime.now().minute == 2:

        df = pd.read_excel('people.xlsx')

        for index, row in df.iterrows():
            send_email()

    time.sleep(60)