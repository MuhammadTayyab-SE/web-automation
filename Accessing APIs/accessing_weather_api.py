import requests
import pandas as pd
from datetime import datetime

def get_weather(city_name, units='metrics',api_key='68e2c17161d5ef46fe0d60ef5177aa38'):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units={units}"
    response = requests.get(url)
    city = []
    time = []
    temprature = []
    condition = []
    data_list = response.json()['list']
    for data in data_list:
        city.append(city_name)
        time.append(str(datetime.utcfromtimestamp(data['dt'])))
        temprature.append(data['main']['temp'])
        condition.append(data['weather'][0]['description'])
    # creating pandas dataframe and saving in csv file
    df = pd.DataFrame({'city':city, 'time':time,'temprature':temprature, 'condition':condition})
    df.to_csv(f"{city_name}_temprature.csv", index=False)
    
get_weather("washington")
