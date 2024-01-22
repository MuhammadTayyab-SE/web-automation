import requests

api_key = '0a3b757badac4d92bb1d6ef465b6e3b8'    
def get_news_on_topic(topic, from_date, to_date, language='en', api_key='0a3b757badac4d92bb1d6ef465b6e3b8'):
    results = []
    # getting news on particular topic
    url = f"https://newsapi.org/v2/everything?q={topic}&from={from_date}&to={to_date}&sortBy=popularity&apiKey={api_key}"
    response = requests.get(url)    
    content = response.json()
    articles = content['articles']
    for article in articles:
        results.append(f"Title:\n{article['title']}: \nDescription:\n{article['description']}\n")
    return results


def get_news_headlines(country, category, api_key='0a3b757badac4d92bb1d6ef465b6e3b8'):
    results = []
    url = f'https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={api_key}'
    response = requests.get(url)    
    content = response.json()
    articles = content['articles']
    for article in articles:
        results.append(f"Title:\n{article['title']}: \nDescription:\n{article['description']}\n")
    return results


# get_news_on_topic("space", from_date="2023-12-27", to_date="2024-01-22")
print(get_news_headlines("us", category='sports')[0])

    
