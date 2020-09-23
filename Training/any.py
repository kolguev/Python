import math

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


"""for j in range(1, 11):
    print([int(i) for i in (lambda x: x * j)("4")])"""


"""number = int(input("Введите число: "))

a = 1
b = 1
l1 = []
l2 = []

for i in range(number):
    l1.append(a)
    a += 1

for j in l1:
    b *= j
    if l1.index(j) % 2 == 0:
        l2.append(b)

s = sum(l2)

print(s)"""


"""def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n


number = int(input("Введите чсло: "))
row = []

for i in range(number + 1):
    if i % 2 != 0:
        row.append(factorial(i))

Sum = 0
for j in row:
    Sum += j

print(
    f"Сумма всех цифр фаториала, стоящих на нечетных позициях длиной {number}, равна {Sum}"
)"""

"""a = [[10, 20, 30, 40, 50], [60, 70, 80, 90, 100]]
row = []

for i in range(len(a)):
    print(a[i])"""

'''a = [['0', '1', '2', '3'], ['4', '5', '6', '7'], ['8', '9', '10', '11'], '2222']

def look_for_key(box):
    for item in box:
        if len(item) > 1:
            look_for_key(item)
        else:
            print(item, end=' ')

look_for_key(a)'''

'''l = [1,3,5,7,9]

def sumList(x):
    if x==[]:
        return 0
    else:
        return x[0]+sumList(x[1:])

print(sumList(l))'''

# Сортировки
# Пузырьковая bubble
'''def bubble_sort(A):
    for i in range(N-1):
        for j in range(N-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

A = [2, 7, 3, 8, 78, 34, 67, 33, 8]
N = len(A)
B = bubble_sort(A)
print(B)
print(B[3] + B[8])

def bubbleSort(l):
    i = 0
    while i<len(l):
        j = 0
        while j<len(l)-1:
            if l[j+1] < l[j]:
                l[j], l[j+1] = l[j+1], l[j]
            j += 1
        i += 1
    return l
a = [93, 12, 67, 77, 12, 81, 88, 58, 72, 55]
b = []
for i in range(len(a)):
    b.append(i)
bubbleSort(a)
print(", ".join(map(str, a)))'''

# Вставками insertion
def insertion(A):
    for i in range(1, len(A)):
        b = A[i]
        j = i - 1
        while (j >= 0) and (b < A[j]):
            A[j+1] = A[j]
            j -= 1
        A[j+1] = b
    return A

arr = [5, 7, 1, 8, 178, 34, 79, 33, 15]
insertion(arr)
arr.reverse()
print(", ".join(map(str, arr)))