import requests
from bs4 import BeautifulSoup
import urllib.parse


# session = requests.session()
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
    "Accept-Language": "ru",
}

text = "монитор 24 дюйма"
text_code = urllib.parse.quote(text)

r = requests.get(
    f"https://www.citilink.ru/search/?text={text_code}&p=1", headers=headers,
).text

soup = BeautifulSoup(r, "html.parser")
span = soup.find_all(
    "div",
    {
        "class": "product_data__gtm-js product_data__pageevents-js ProductCardVertical js--ProductCardInListing ProductCardVertical_normal ProductCardVertical_shadow-hover"
    },
)

with open("citilink.txt", mode="w", encoding="utf8") as code:
    code.write(str(span[1]))
