def sum(a,b):
    print("sum of tow number is ",a+b)
n=int(input("enter the num1:-"))
m=int(input("enter the num1:-"))
sum(n,m)

#set defautl value in argument
def sum(a,b=10):
    print(int(a+b))
sum(10)                                         #a=10,b=10 b's default value is 10

def sum(a,b=1):
    print(int(a+b))
sum(10,20)