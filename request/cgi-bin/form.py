#!/usr/local/bin/python3
import requests

# from bs4 import BeautifulSoup
# import json
import cgi

form = cgi.FieldStorage()
url = form.getfirst("uri", "not defined")

p1k = form.getfirst("param1-key", "not defined")
p1v = form.getfirst("param1-value", "not defined")

p2k = form.getfirst("param2-key", "not defined")
p2v = form.getfirst("param2-value", "not defined")

p3k = form.getfirst("param3-key", "not defined")
p3v = form.getfirst("param3-value", "not defined")

######################################
# Дальше пример ключей и значений
# HeadersKey = {
#    "accept": "aplication/json",
#    "email": "your-email",
#    "password": "your-pass",
# }

HeadersKey = {p1k: p1v, p2k: p2v, p3k: p3v}  # Параметры для получения ключа
Key = requests.get(
    "http://petfriends1.herokuapp.com/api/key", headers=HeadersKey
).json()

HeadersPets = {
    p1k: p1v,
    "auth-key": Key["key"],
}  # Параметры для заголовка на получение данных по животным

GetMyPets = requests.get(
    "http://petfriends1.herokuapp.com/api/pets?filter=my_pets", headers=HeadersPets
).text

string2 = ""
width = 100
L = len(GetMyPets) // 100
L2 = len(GetMyPets)
F = 0

for i in range(1, L + 2):
    string2 = string2 + GetMyPets[F : i * 100] + "\n"
    F = i * 100

print("Content-type: text/html\n")
print(
    """<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Form Data</title>
            <link rel="stylesheet" type="text/css" href="../style.css">
        </head>
        <body>
        <div class="page-wrapper">
        """
)

print("<h1>Form Data!</h1>")
print("<p>L: {}</p>".format(L2))
print("<p>url: {}</p>".format(url))
print("<p>p1k: {}</p>".format(p1k))
print("<p>p1v: {}</p>".format(p1v))
print("<p>p2k: {}</p>".format(p2k))
print("<p>p2v: {}</p>".format(p2v))
print("<p>p3k: {}</p>".format(p3k))
print("<p>p3v: {}</p>".format(p3v))
print("<p>MyPets: {}</p>".format(string2))
print(
    """</div>
            </body>
                </html>"""
)

