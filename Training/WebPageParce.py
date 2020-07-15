import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.sport-express.ru/')
soup = BeautifulSoup(r.content.decode('utf-8'), 'lxml')
t = r.text
print(t)
print(r.status_code)