# maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]

l = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# ind = 0

for ind in range(0, len(l)):
    SumList = [sum(l[ind:x]) for x in range(1, len(l) + 1)]

    # SumList = [sum(l[ind:x]) for x in range(1, len(l) + 1)]
    # AnyList = [[sum(l[ind:x]), l[ind:x]] for x in range(1, len(l) + 1)]
    # AnyList2 = [l[ind:x] for x in range(1, len(l) + 1)]
    print(SumList)
    # print(AnyList2)
