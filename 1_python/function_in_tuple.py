#min()   give min value in tuple
from itertools import count


t=(1,2,3,4,5,1)
print(min(t))

#max()   give max value in tuple
print(max(t))

#count()  give repated value in tuple
a=t.count(1)
print(a)

#index    give index number in tuple
b=t.index(2)       # here  put element to know index number
print(b)

# sum    give sum of all integer in tuple not string

print(sum(t))

print(sum(t,10))     # here t=16 but now 10 more value is add