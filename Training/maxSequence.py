# should be 6: [4, -1, 2, 1]

maxSequence = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def maxSequence(arr)
maxSequence2 = []
for ind in range(0, len(maxSequence)):
    maxSequence2.append(
        max(
            [
                [sum(maxSequence[ind:x]), maxSequence[ind:x]]
                for x in range(ind + 1, len(maxSequence) + 1)
            ]
        )
    )

print(": ".join([str(elem) for elem in max(maxSequence2)]))
