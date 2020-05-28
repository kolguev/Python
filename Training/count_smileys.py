# codewars.com kata Count the smiley faces!
# should be 6: [4, -1, 2, 1]

import re

l =  [';D', ':-(', ':-)', ';~)']

# for x in range(len(l)):
#     if l[x].find(';-D') == 0:
#         print(x)

def count_smileys(arr):
    Count = []
    for x in l:
        result = re.findall(r'[;|:][-|~]?[)|D]$', x)
        if result:
            Count.append(result)
    return len(Count)

count_smileys(l)
#print(",".join(l))

# result = re.search("i", 'rfirjirfrjfijrf:)')
# print(result.group(0))