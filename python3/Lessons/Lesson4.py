'''book = {"a": 1,"b": 2,"c": 3}
print book

book["s"]=12

print book
del book["a"]
print book

book["b"]=9
print book

b = book.pop("b")

print book, b

import math
import random
list = [math.floor(random.random()*10) for x in range(5)]
list2 = [math.floor(random.random()*10) for x in range(7)]
print list, "\n", list2

list = set(list)
list2 = set(list2)
print list, "\n", list2
print "union", list.intersection_update(list2)
print lis'''

tuple = tuple("HELLO WOTLD!")
print type(tuple), tuple

print "".join(tuple)



