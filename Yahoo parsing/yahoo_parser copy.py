import requests
from bs4 import BeautifulSoup
import json

def get_fin_info(ticker):
    lticker = ticker.lower()
    url = f'https://finance.yahoo.com/quote/{lticker}/key-statistics?p={lticker}'
    headers = {
        'accept': '*/*',
        'origin': 'https://finance.yahoo.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }
    req = requests.get(url, headers = headers)
    src = req.text
    #print(src)

    with open(f'{lticker}-yahoo-finance.html', 'w', encoding='utf-8') as file:
        file.write(src)

    with open(f'{lticker}-yahoo-finance.html', encoding='utf-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'html.parser')

    tables = soup.find_all({"table": "W(100%) Bdcl(c)", })
    d = {}
    list_values = []
    for table in tables:
        values = table.find_all('td')
        for value in values:
            list_values.append(value.text)

    for i in range(0, len(list_values), 2):
        string = list_values[i][:list_values[i].rindex(" ")]
        d[string] = list_values[i + 1]

    with open('financial_data.json', 'w') as file:
        json.dump(d, file, indent=4, ensure_ascii=False)

    return(d)
