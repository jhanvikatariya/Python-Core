#request
#API=Application Program Interface
import requests
response=requests.get('https://www.geeksforgeeks.org/')
print(response.text)

url='https://jsonplaceholder.typicode.com/posts'
data={
    'title':'bhumi',
    'body':'bhai',
    'userID':12    
}
headers={
    'Content-type':'application/json; charset=UTF-8',
}
response=requests.post(url,headers=headers,json=data)
print(response.text)