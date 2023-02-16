t=[10,20,30,40]
print(type(t))

t=(10)
print(type(t))            # in tuple element always more than one 

# how to iterate tuple
t=(1,2,3,4,5,6)
a=len(t)
b=t[0:]
for i in range(a):
    print(t[i])
print()

# part2
for n in t:
    print(n)
print()

#part2
for m in b:
    print(m)
