import math
x, y, z = 3, 6.5, 15
c = y**2 + abs((x**2)/(y + (x**3)/3))
a = y + (x/c)
b = 1 + math.tan(z/2)**2
print("up a =", math.floor(a))
print("up b =", math.floor(b))
print("up a =", math.ceil(a))
print("up b =", math.ceil(b))