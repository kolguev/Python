import requests
import cgi

Headers = {"accept": "aplication/json", "email": "alexseym@inbox.ru", "password": "qwe123!"}

#HeadersKey = {p1k: p1v, p2k: p2v, p3k: p3v} # Параметры для получения ключа
Key = requests.get("http://petfriends1.herokuapp.com/api/key", headers=Headers).json()
print(Key["key"])

HeadersPets = {"accept": "aplication/json", "auth-key": Key["key"]} # Параметры для заголовка на получение данных по животным

GetMyPets = requests.get("http://petfriends1.herokuapp.com/api/pets?filter=my_pets", headers=HeadersPets).json()
print(GetMyPets["pets"])
