string = "Dismental"

def isogram(string):
    s = set(string)
    for i in s:
        c = string.count(i)
        if c > 1:
            return False


print(isogram(string))


string = "Dismental"
s = set(string)
l = {string}
c = s - l
print(c)
