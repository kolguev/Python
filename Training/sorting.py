from operator import itemgetter
import time

l = ["Type", "hello", "Alex", "3", "Russia", "my", "i2"]

l.sort(reverse=True)
sorted_l = sorted(l, key=str.upper)


print(l)
print(sorted_l)

student_tuples = [
    ("john", "A", 15),
    ("jane", "B", 12),
    ("dave", "B", 10),
]

m1 = [1, 3, 5, 7, 9]
m2 = [4, 10, 8, 6, 2]


def merge(a, b):
    for i in b:
        a.append(i)

    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


print(merge(m1, m2))


m3 = [10, 15, 4, 8, 6, 2]
print(len(m3))
time1 = time.time()

for e in range(len(m3) - 1):
    for i in range(len(m3) - 1 - e):
        if m3[i] > m3[i + 1]:
            m3[i], m3[i + 1] = m3[i + 1], m3[i]

time2 = time.time()

print(time1)
print(time2)
print(m3)

