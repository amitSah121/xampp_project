import requests

url = "http://103.211.202.111/backend/main.py?make=hello12345" # 'https://w3schools.com'
x = requests.get(url)
print(x,x.text)