# codewars.com kata Count the smiley faces!
# should be 6: [4, -1, 2, 1]

import re

l = [":)", ":-)", ";-(", "-)"]


def count_smileys(arr):
    c = []
    for x in arr:
        result = re.findall(r"[;|:][-|~]?[)|D]$", x)
        if result:
            c.append(result)
    return len(c)


count_smileys(l)
