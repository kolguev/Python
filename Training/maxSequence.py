# codewars.com kata Maximum subarray sum
# should be 6: [4, -1, 2, 1]

# l = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
l = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


def maxSequence(arr):
    arr2 = []
    if arr:
        for ind in range(0, len(arr)):
            arr2.append(max([[sum(arr[ind:x]), arr[ind:x]] for x in range(ind + 1, len(arr) + 1)]))
        if max(arr2)[0] > 0:
            return max(arr2)[0]
        else:
            return 0
    else:
        return 0

print(maxSequence(l))

def MaxSequence(arr):
    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    return max
