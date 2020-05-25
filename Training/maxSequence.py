# maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
s = [sum(l[ind:x]) for x in range(1, len(l) + 1)]
d = {s: l[ind:x]}

l = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
ind = 0
for x in range(1, len(l) + 1):
    s = sum(l[ind:x])
    d = {s: l[ind:x]}
    print(d)
