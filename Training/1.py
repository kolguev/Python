string = "топот рокот стук колес роза ветер 141 4434 тот"

l = string.split()
print(l)
l2 = []

for i in l:
    if i == i[::-1]:
        l2.append(i)

print(l2)
