string = "Dismental"

def isogram(string):
    for i in string:
        c = string.count(i)
        if c > 1:
            return False
    return True

print(isogram(string))

def isogram1(string):
    return len(string) == len(set(string))
print(isogram1(string))