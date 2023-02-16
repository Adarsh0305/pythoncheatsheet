a=[10,20,30,40,50]
t=a[-1::-1]
b=len(a)

for i in range(b-1,-1,-1):
    print(a[i])
print()

for n in t:
    print(n)
