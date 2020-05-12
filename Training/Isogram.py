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
<<<<<<< HEAD
if s == list(string):
    print(True)
=======
l = {string}
c = s - l
print(c)
>>>>>>> 540ee52c366249c948a8932c58116bccba9f4766
