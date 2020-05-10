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
    # for i in a:
    #     b = str(b)
    #     CountOfI = b.count(i)
    #     start = 0
    #     for item in range(0, CountOfI):
    #         simbol = b.find(i,start,len(b))
    #         print(simbol)
    #         start = simbol + 1
            # b = b[simbol+1:len(b)]
            # if b[item] == i:
            #     index = b.find(i)
            #     print(index)
            #     b = b[index+1:len(b)]
            #     print(b)
            # else:
            #     print("No")
    NeedString = a + b
    s = sorted(NeedString)
    s = "".join(s)
    print(s)
    for i in s:
        if i in s:
            print(i)



first = "xyaabbbccccdefww"
second = "xxxxyyyyabklmopq"
# first = "x"
# second = "xyyx"
IndexOFF(first,second)