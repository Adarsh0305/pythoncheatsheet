   # by usning appent() function

a=[]

for i in range(1,11):
    print(i)
print()

for n in range(1,11):
    a.append(n)
print(a)

        # shortcut mathod to create list

n=[a for a in range(1,11)]
print(n)

m=[n for n in range(1,11) if n%2==0]     # here how to apply filter 
print(m)

b=[]
for i in range(1,11):         # for normal method 
    if i%2==0:  
      b.append(i)
print(b)
