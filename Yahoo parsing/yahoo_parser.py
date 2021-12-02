import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

# https://finance.yahoo.com/quote/TSLA/analysis?p=TSLA
# div class="B(8px) Pos(a) C(white) Py(2px) Px(0) Ta(c) Bdrs(3px) Trstf(eio) Trsde(0.5) Arrow South Bdtc(i)::a Fw(b) Bgc($buy) Bdtc($buy)"

def get_fin_info(ticker):
    lticker = ticker.lower()
    url_stat = f'https://finance.yahoo.com/quote/{lticker}/key-statistics?p={lticker}'
    url_analys = f'https://finance.yahoo.com/quote/{lticker}/analysis?p={lticker}'
    headers = {
        'accept': '*/*',
        'origin': 'https://finance.yahoo.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }
    req = requests.get(url_stat, headers = headers)
    src = req.text

    # Get recommendation
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(executable_path='chromedriver', options=options)
    driver.get(url_analys)
    time.sleep(2)
    #driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    driver.execute_script("window.scrollTo(0, 600)")
    time.sleep(1)
    recommendation_status = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]").text
    time.sleep(1)
    driver.quit()
    if 1 <= float(recommendation_status) < 2:
        recommendation_status = f'{recommendation_status} Strong By'
    elif 2 <= float(recommendation_status) < 3:
        recommendation_status = f'{recommendation_status} By'

    #

    with open(f'{lticker}-yahoo-finance.html', 'w', encoding='utf-8') as file:
        file.write(src)

    with open(f'{lticker}-yahoo-finance.html', encoding='utf-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'html.parser')

    tables = soup.find_all({"table": "W(100%) Bdcl(c)", })
    finance_info = {}
    list_values = []
    for table in tables:
        values = table.find_all('td')
        for value in values:
            list_values.append(value.text)

    if list_values[0] == 'Market Cap (intraday) 5':
        for i in range(0, len(list_values), 2):
            key_string = list_values[i][:list_values[i].rindex(" ")]
            finance_info[key_string] = list_values[i + 1]
    else:
        return('Info not found.')

    with open('financial_data.json', 'w') as file:
        json.dump(finance_info, file, indent=4, ensure_ascii=False)

    out_info = ['52 Week High','52 Week Low', 'Revenue Per Share']

    return(f'{out_info[0]}: {finance_info[out_info[0]]} \n{out_info[1]}: {finance_info[out_info[1]]} \n{out_info[2]} (ttm): {finance_info[out_info[2]]} \n{recommendation_status}')
