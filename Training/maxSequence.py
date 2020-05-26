# should be 6: [4, -1, 2, 1]

l = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


def maxSequence(arr):
    arr2 = []
    for ind in range(0, len(arr)):
        arr2.append(
            max([[sum(arr[ind:x]), arr[ind:x]] for x in range(ind + 1, len(arr) + 1)])
        )
    return ": ".join([str(elem) for elem in max(arr2)])


print(maxSequence(l))
