import requests
from bs4 import BeautifulSoup
import json

HeadersKey = {
    "accept": "aplication/json",
    "email": "alexseym@inbox.ru",
    "password": "qwe123!",
}

GetKey = requests.get("http://petfriends1.herokuapp.com/api/key", headers=HeadersKey)
Key = GetKey.text
AuthKey = Key[(Key.find(":") + 2) : (len(Key) - 3)]
print(Key)
print(AuthKey)

HeadersPets = {"accept": "aplication/json", "auth-key": AuthKey}

# print(HeadersPets)

GetMyPets = requests.get(
    "http://petfriends1.herokuapp.com/api/pets?filter=my_pets", headers=HeadersPets
)
Pets = GetMyPets.text
print(Pets[0:200])

