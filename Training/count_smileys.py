# codewars.com kata Count the smiley faces!
# should be 6: [4, -1, 2, 1]

import re

l =  [';]', ':[', ';*', ':$', ';-D']
l2 = [ ':)', ';)', ':~)', ':-)', ';~)', ';-)', ':D', ';D', ':~D', ':-)D', ';~D', ';-D' ]

# for x in range(len(l)):
#     if l[x].find(';-D') == 0:
#         print(x)

for x in l:
    result = re.findall(r'[;|:][-|~][D|)]', x)
    if result:
       print(result)

#print(",".join(l))

# result = re.search("i", 'rfirjirfrjfijrf:)')
# print(result.group(0))