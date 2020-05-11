Strings = "6767879988787867576"

def maskifi(String):
    if len(String) > 4:
        String1 = String[:-4]
        String2 = String[-4:]
        String3 = len(String1)
        String4 = String1.replace(String1, "#" * String3) + String2
        print(String4)
    else:
        print(String)

maskifi(Strings)