l=[10,20,30,40]
l2=[50,60,70,80]

for a,b in zip(l,l2):
    print(a,b)              # zip function print 2 list at same time

print()
# other case in zip function

l1=[1,2,3]
m=[4,5,6,7]

for x,y in zip(l1,m):
    print(x,y)

print()
# without using zip function

p=[0,3,0,5]
q=[2,0,0,3]
t=len(p)

for n in range(t):
    print(p[n],q[n])


