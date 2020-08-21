import re

mail = input("Input email: ")

for i in mail:
    result = re.findall(r"(^\w\w+[@]\w\w+[\.][a-z][a-z]+$)", mail)
    if result:
        print({result[0]: "True"})
    else:
        print("Wrong email")
