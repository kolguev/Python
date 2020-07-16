import requests
from bs4 import BeautifulSoup
import json
import cgi

form = cgi.FieldStorage()
uri = form.getfirst("uri", "not defined")

p1k = form.getfirst("param1-key", "not defined")
p1v = form.getfirst("param1-value", "not defined")

p2k = form.getfirst("param2-key", "not defined")
p2v = form.getfirst("param2-value", "not defined")

p3k = form.getfirst("param3-key", "not defined")
p3v = form.getfirst("param3-value", "not defined")

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>uri: {}</p>".format(uri))
print("<p>param1-key: {}</p>".format(p1k))
print("<p>param1-value: {}</p>".format(p1v))
print("<p>param2-key: {}</p>".format(p2k))
print("<p>param2-value: {}</p>".format(p2v))
print("<p>param3-key: {}</p>".format(p3k))
print("<p>param3-value: {}</p>".format(p3v))


print("""</body>
        </html>""")


######################################

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

