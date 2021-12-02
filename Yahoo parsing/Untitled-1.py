import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# https://finance.yahoo.com/quote/TSLA/analysis?p=TSLA
# div class="B(8px) Pos(a) C(white) Py(2px) Px(0) Ta(c) Bdrs(3px) Trstf(eio) Trsde(0.5) Arrow South Bdtc(i)::a Fw(b) Bgc($buy) Bdtc($buy)"

url = 'https://finance.yahoo.com/quote/mrk/analysis?p=mrk'
    
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
driver = webdriver.Chrome(executable_path='chromedriver', options=chrome_options)
driver.get(url)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(1)
name = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]").text

print(name)
#print(src)
#with open(f'aapl-yahoo-finance.html', 'w', encoding='utf-8') as file:
#    file.write(src)

#with open(f'aapl-yahoo-finance.html', encoding='utf-8') as file:
#    src = file.read()

#soup = BeautifulSoup(src, 'html.parser')

#tables = soup.find_all({"class": "B(8px) Pos(a) C(white) Py(2px) Px(0) Ta(c) Bdrs(3px) Trstf(eio) Trsde(0.5) Arrow South Bdtc(i)::a Fw(b) Bgc($c-fuji-teal-2-b) Bdtc($c-fuji-teal-2-b)", })
#regex = re.compile('B(8px) Pos(a) C(white) Py(2px) Px(0) Ta(c) Bdrs(3px) Trstf(eio) Trsde(0.5) Arrow South Bdtc(i)*')
#tables = soup.find_all("div", {"class": 'B(8px) Pos(a) C(white) Py(2px) Px(0) Ta(c) Bdrs(3px) Trstf(eio) Trsde(0.5) Arrow South Bdtc(i)::a Fw(b) Bgc($c-fuji-teal-2-b) Bdtc($c-fuji-teal-2-b)'})
#print(tables)

