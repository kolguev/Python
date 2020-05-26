# maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]

l = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

l2 = []
for ind in range(0, len(l)):
    l2.append(max([[sum(l[ind:x]), l[ind:x]] for x in range(ind + 1, len(l) + 1)]))
    # ListOfSequences = [l[ind:x] for x in range(ind + 1, len(l) + 1)]
    # print(AnyList)
    # print(max([sum(l[ind:x]) for x in range(ind + 1, len(l) + 1)]))
print(max(l2))
