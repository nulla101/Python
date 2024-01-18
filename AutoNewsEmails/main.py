import yagmail
import pandas
from news import NewsFeed
import datetime
import time


def send_email():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    news_feed = NewsFeed(interest=row['interest'],
                         from_date=yesterday,
                         to_date=today,
                         language=row['language'])
    email = yagmail.SMTP(user="nullanulla101@gmail.com",
                         password="bdzgshthhoqkkpvc")
    email.send(to=row['email'],
               subject=f"Your {row['interest']} news for today!",
               contents=f"Hi {row['name']},\n See what's new on {row['interest']} today!"
                        f"\n\n {news_feed.get()}\nNoella")


while True:

    if datetime.datetime.now().hour == 10 and datetime.datetime.now().minute == 30:
        df = pandas.read_excel('people.xlsx').dropna()

        for index, row in df.iterrows():
            send_email()
    time.sleep(60)
