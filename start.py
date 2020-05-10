# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"
#
# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"

def IndexOFF(a, b):
#    IndexValue = 0
    for i in a:
        b = str(b)
        CountOfI = b.count(i)
        for item in range(1, CountOfI):
            if i in b:
#                index = a.find(i)
#                IndexValue = IndexValue + 1
#                print(IndexValue)
                print(i)
                index = b.find(i)
                print(index)


first = "xyaabbbccccdefww"
second = "xxxxyyyyabklmopq"
IndexOFF(first,second)