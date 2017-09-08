import math
from decimal import Decimal
x, y, z = 1, 2, 3
e = math.sqrt(abs(x-1))-math.sqrt(abs(y))**3
a = e/(1 + (x**(2/2) + y**(2/4)))
print("a =", a)
b = (x*(math.atan(z) + e**(-(x+3))))
print("b =", b)