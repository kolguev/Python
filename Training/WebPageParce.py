import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.sport-express.ru/')
t = r.text
print(t)
print(r.status_code)