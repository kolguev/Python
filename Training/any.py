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


# img = Image.open("1.png")
# img.format
vklad = 100000
month = 12
percent = 0.033

"""for i in range(0, month):
    MonthSum = vklad * (percent / month)
    vklad = vklad + MonthSum
print(vklad)"""

i = 0
while i < month:
    vklad += vklad * (percent / month)
    i += 1
print(vklad)
