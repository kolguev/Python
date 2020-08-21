import re

mail = input("Input email: ").split(", ")
print(type(mail))
dict_email = {}
for i in mail:
    result = re.findall(r"(^\w\w+[@]\w\w+[\.][a-z][a-z]+$)", i)
    if result:
        dict_email[i] = True  # print({result[0]: "True"})
    else:
        print("Wrong email")

print(dict_email)
