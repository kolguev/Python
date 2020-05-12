string = "Dismental"

def isogram(string):
    for i in s:
        c = string.count(i)
        if c > 1:
            return False
    return True

print(isogram(string))