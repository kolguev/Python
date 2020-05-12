def maskify1(String):
    if len(String) > 4:
        String1 = String[:-4]
        String2 = String[-4:]
        String3 = len(String1)
        String4 = String1.replace(String1, "#" * String3) + String2
        print(String4)
    else:
        print(String)



Strings = "6767"
maskify1(Strings)

print(Strings[:-4].replace(Strings[:-4], "#" * len(Strings[:-4])) + Strings[-4:])

print('#' * (len(Strings) - 4) + Strings[-4:])