string = "Dissmental"

def isogram(string):
    for i in string:
        c = string.count(i)
        if c > 1:
            return False
    return True

print(isogram(string))


