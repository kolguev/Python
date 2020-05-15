def find_even_index(arr):
    for i in arr:
        #IndexOfI = arr.index(i) # integer
        #Sum0 = sum(arr[0:arr.index(i)]) # list
        #Sum1 = sum(arr[(arr.index(i) + 1):len(arr)]) # list
        if sum(arr[0:arr.index(i)]) == sum(arr[(arr.index(i) + 1):len(arr)]):
            return arr.index(i)
    return -1



ListOfInteger = [1,2,3,4,3,2,1]
""" Sum0 = sum(ListOfInteger[0:6]) # list
Sum1 = sum(ListOfInteger[(6 + 1):len(ListOfInteger)]) # list
print(Sum1) """

print(find_even_index(ListOfInteger))