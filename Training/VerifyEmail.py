import re

mail = input("Input email: ").split(", ")

dict_email = {}

for i in mail:
    dict_email[i] = False

    result = re.findall(r"(^\w\w+[@]\w\w+[\.]?\w\w+[\.][a-z][a-z]+$)", i)
    if result:
        dict_email[i] = True

print(dict_email)
