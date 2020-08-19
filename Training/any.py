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


text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum eget tempus est. Phasellus sit amet 
tristique neque. Sed luctus mi ut nisi suscipit placerat. Nunc nec diam dapibus, fermentum risus ut, ultrices orci. 
Integer non magna molestie nibh dapibus tincidunt. Quisque quis est quam. Sed dictum mi sit amet magna pretium blandit. 
Nulla tortor turpis, maximus vitae lobortis quis, varius sed metus. Nullam at congue metus. Pellentesque scelerisque, dui 
et luctus semper, odio diam scelerisque justo, nec tempor ex metus et enim. Praesent rhoncus nisl eget risus elementum ornare. 
Praesent tellus mauris, viverra vitae malesuada at, ornare id nisi. Vestibulumi."""

text = text.replace(" ", "").lower()
most_common = None
qty_most_common = 0
d = {}
l = []

for item in set(text):
    qty = text.count(item)
    l.append(qty)
    d.update({qty: item})

l = sorted(l)
needLetter = (l[len(l) - 2 : -1])
print(d[needLetter[0]])