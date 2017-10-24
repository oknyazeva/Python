t = tuple("Hello World!")
print ("string =",''.join(t))
print t.count(t[0])
l = list(t)
print ("List =", l)

for x in range(1,len(l), 2):
    l[x] = -1
print l

