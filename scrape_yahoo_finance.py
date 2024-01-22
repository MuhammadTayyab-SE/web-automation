import requests
from datetime import datetime as dt
import time
ticker = input("Enter the ticker symbol: ")
from_date = input('Enter Start Date in yyyy/mm/dd format: ')
to_date = input('Enter End Date in yyyy/mm/dd format: ')

from_datetime = dt.strptime(from_date, '%Y/%m/%d')
to_datetime = dt.strptime(to_date, '%Y/%m/%d')

# convert time to epoch
from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))


url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"

# we need to add header so that our request acts like a browser request
headers= {"User-Agent": "Mozilla/53.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

# .content method return byte object so we can download files, audio files etc.
content = requests.get(url, headers=headers).content

with open(f"{ticker}.csv",'wb') as file:
    file.write(content)