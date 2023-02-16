s={10,20,30}
print(s)

# how to iterate 
for i in s:
    print(i)

# function in set
# 01 set()         convert list or tuple to set

l=[10,20,30]
s=set(l)
print(s)

# 03 add()     add new element in set
s={10,20,30}
s.add(40)
print(s)

#pop()    remove any element in set
a={10,20,30}
print(a.pop())
print(a)

# remove     remove element whose we want
i={10,20,30}
i.remove(10)
print(i)

# clear    clear all set
j={10,20,30}
j.clear()
print(j)

# discard       same as remove
k={10,20,30}
k.discard(30)
print(k)

# update     update element in set from list and tuple
x=[10,20,30]
s={40,50,60}
s.update(x)
print(s)

y={10,20,30}
y.update(40)
print(y)

