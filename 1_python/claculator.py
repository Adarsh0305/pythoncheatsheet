x=eval(input("enter the first value : "))
op=input("enter the operator : ")
y=eval(input("entre the second value : "))

if op=='+':
    print('ans is',x+y)

if op=='-':
    print('ans is ',x-y)


if op=='*':
    print('ans is ',x*y)

if op=='/':
    print('ans is ',x/y)

else:
    print("invalid operation")