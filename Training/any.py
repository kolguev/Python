# from PIL import Image

# print(sys.version)
# print(sys.executable)

# number_list = []
# for number in range(1100, 5, -58):
#     number_list.append(number)
# print(number_list)

# word = "letters"
# print(set(word))
# letter_counts = {letter: word.count(letter) for letter in set(word)}
# print(letter_counts)


'''text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum eget tempus est. Phasellus sit amet 
tristique neque. Sed luctus mi ut nisi suscipit placerat. Nunc nec diam dapibus, fermentum risus ut, ultrices orci. 
Integer non magna molestie nibh dapibus tincidunt. Quisque quis est quam. Sed dictum mi sit amet magna pretium blandit. 
Nulla tortor turpis, maximus vitae lobortis quis, varius sed metus. Nullam at congue metus. Pellentesque scelerisque, dui 
et luctus semper, odio diam scelerisque justo, nec tempor ex metus et enim. Praesent rhoncus nisl eget risus elementum ornare. 
Praesent tellus mauris, viverra vitae malesuada at, ornare id nisi. Vestibulum."""

text = text.replace(" ", "").lower()
lt = []
l = []

for item in set(text):
    qty = text.count(item)
    l.append(qty)
    t = (qty, item)
    lt.append(t)

l = sorted(l)
needLetter = l[len(l) - 2 : -1]

for item in lt:
    if item[0] == needLetter[0]:
        print(item[1])'''

"""list_email = input("Enter emails: ").split(", ")
dict_email = {}

for i in list_email:
    result = False

    if "@" in i and i.count("@") >= 1:
        name = i.split("@")[0]
        if len(name) >= 2:
            domen = i.split("@")[1]
            if "." in domen:
                if len(domen.split(".")[0]) >= 2:
                    result = True

    dict_email[i] = result

print(dict_email)"""


"""l = [4]

for j in range(10):
    print([i for i in l])
    l.append(4)"""


for j in range(1, 11):
    print([int(i) for i in (lambda x: x * j)("4")])
