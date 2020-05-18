String = "This website is for losers LOL!"

def disemvowel(string):
    s = 'aeioquAEIOQU'
    for item in s:
        i = string.find(item)
        if i > 0:
            string = string.replace(string[i], '')
    return string


print(disemvowel(String)