# install flask package by 
# pip install flask
from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

def get_currency(in_currency, out_currency):
    url = f"https://x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    page_content = requests.get(url).text
    soup = BeautifulSoup(page_content, 'html.parser')
    cur_rate = soup.find("span", class_='ccOutputRslt').get_text()[:-4]
    return float(cur_rate)


# defining flask object
app = Flask(__name__)

# Adding home route
@app.route('/')
def home():
    return """
            <h1>Currency Rate API</h1>
            <p>This is paragraphed currency</p>  
            <p> Example URL: /api/v1/usd-eur</p>
        """
@app.route('/api/v1/<in_cur>-<out_cur>')
def curreny_conversion_rate(in_cur, out_cur):
    rate = get_currency(in_cur, out_cur)
    res_dict = {'input_currency':in_cur, 'output_currency':out_cur, 'rate':rate}
    return jsonify(res_dict)
        
        
app.run(host='0.0.0.0')