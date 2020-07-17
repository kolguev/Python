import requests
#from bs4 import BeautifulSoup
#import json
import cgi

form = cgi.FieldStorage()
url = form.getfirst("uri", "not defined")

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
            <title>Form Data</title>
        </head>
        <body>""")

print("<h1>Form Data!</h1>")
print("<p>url: {}</p>".format(url))
print("<p>p1k: {}</p>".format(p1k))
print("<p>p1v: {}</p>".format(p1v))
print("<p>p2k: {}</p>".format(p2k))
print("<p>p2v: {}</p>".format(p2v))
print("<p>p3k: {}</p>".format(p3k))
print("<p>p3v: {}</p>".format(p3v))

print("""</body>
        </html>""")


######################################
# Дальше пример ключей и значений
#HeadersKey = {
#    "accept": "aplication/json",
#    "email": "your-email",
#    "password": "your-pass",
#}

HeadersKey = {p1k: p1v, p2k: p2v, p3k: p3v} # Параметры для заголовка на получение ключа

GetKey = requests.get(url, headers=HeadersKey)
Key = GetKey.text
AuthKey = Key[(Key.find(":") + 2) : (len(Key) - 3)]
print(Key)
#print(AuthKey)

HeadersPets = {p1k: p1v, "auth-key": AuthKey} # Параметры для заголовка на получение данных по животным

GetMyPets = requests.get(
    "http://petfriends1.herokuapp.com/api/pets?filter=my_pets", headers=HeadersPets
)
MyPets = GetMyPets.text
print(MyPets)
