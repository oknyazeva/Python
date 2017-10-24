n = 123
a = int(n/100)
b = int((n/10) - (a*10))
c = int(n - (a*100 + b*10))
print("a = ", a)
print("b = ", b)
print("c = ", c)
print("a + b + c = ", a + b + c)
