import re

mail = input("Input email: ").split(", ")

dict_email = {}
for i in mail:
    result = re.findall(r"(^\w\w+[@]\w\w+[\.][a-z][a-z]+$)", i)
    if result:
        dict_email[i] = True  # print({result[0]: "True"})
    else:
        dict_email[i] = False  # print("Wrong email")

print(dict_email)
