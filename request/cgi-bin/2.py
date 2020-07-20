string = "keoiekddjedufrgfrhudjksdmknfjfbfguhguiriekdlsmdnfjhuthgutyeifsekdsnfdvhugriofjoedklsmcdkfnhgrjgikfl;elsdlmdkfkgrgurghuvnjvnjrnkkfkngsjiwaeuiwoyrueytrughfjnckdlcmslkiruitrywoewq[ep[[ldkfldjfkgfknbmbnmv,,xcmzkjiryueyturgjfdjksjfskjdieryuturgbfnvmc,xczmkleiwureiyruhrkjkmflmvkfvntgjir"

string2 = ""
width = 100

# while width > 0:

string2 = string2 + string[:width] + "\n"
string2 = string2 + string[width : (width + 100)] + "\n"
string2 = string2 + string[(width + 100) :]

print(string)
print(len(string2))
