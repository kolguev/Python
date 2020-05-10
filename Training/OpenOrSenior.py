import sys
print(sys.version)
print(sys.executable)


# data = [[55, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9],[37,7], [61,15]]
data = [[33, -1], [64, 3], [33, 13], [73, 27], [64, 3], [66, 23]]

def openOrSenior(data):
    NewData = []
    for Item in data:
        if Item[0] >= 55 and Item[1] > 7 and Item[1] <= 26:
            Item = "Senior"
            NewData.append(Item)
        else:
            Item = "Open"
            NewData.append(Item)
    return NewData

print(openOrSenior("data"))