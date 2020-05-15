def find_even_index(arr):
    for i in arr:
        if sum(arr[0:arr.index(i)]) == sum(arr[(arr.index(i) + 1):len(arr)]):
            return arr.index(i)
    return -1

ListOfInteger = [0,0,0,0,0] #list(range(1,100)) #[10,-80,10,10,15,35,20]

print(find_even_index(ListOfInteger))