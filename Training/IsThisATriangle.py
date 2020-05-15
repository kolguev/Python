def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False

a = 7
b = 2
c = 2

print(is_triangle(a, b, c))