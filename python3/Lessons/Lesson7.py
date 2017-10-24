'''
import math
def f(a1,b1,c1):
    print a1, b1, c1
    return a1+b1+c1
f(1,1,1)
print f(1,2,3)

def f1(a,b,c=1):
    return (2*a-b + math.sin(c)/(5+math.fabs(c)))
s=1
t=2
print f1(t,-2*s, 1.17) + f1(2.2, t, s - t)
'''
from Mod import mod1
print mod1.f(1,2,3)
