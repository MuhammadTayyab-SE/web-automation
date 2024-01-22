import requests
from bs4 import BeautifulSoup

def get_currency(in_currency, out_currency):
    url = f"https://x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    page_content = requests.get(url).text
    soup = BeautifulSoup(page_content, 'html.parser')
    cur_rate = soup.find("span", class_='ccOutputRslt').get_text()[:-4]
    return float(cur_rate)
get_currency('USD','EUR')