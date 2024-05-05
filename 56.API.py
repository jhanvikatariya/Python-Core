import requests
import json
url='https://newsapi.org/v2/everything?q=tesla&from=2024-04-07&sortBy=publishedAt&apiKey=31e77bbe3c3f48b39b95296993ed23af'
r=requests.get(url)
news=json.loads(r.text)

for article in news['articles']:
    print(article['title'])
    print(article['description'])
    print('------------------------')