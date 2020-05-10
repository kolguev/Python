def disemvowel(string):
    a = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in string:
        if i in a:
            string = i="" 
    print(string)

disemvowel("Hello Aorld")



