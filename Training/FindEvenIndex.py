def find_even_index(arr):
    Number = 0
    for i in arr:
        if sum(arr[0:Number]) == sum(arr[(Number + 1):len(arr)]):
            return Number
        Number += 1
    return -1

ListOfInteger = [20,10,30,10,10,15,35]
print(find_even_index(ListOfInteger))

#Sum0 = sum(ListOfInteger[0:3])
#Sum1 = sum(ListOfInteger[(3 + 1):len(ListOfInteger)])
#print(Sum0 == Sum1)