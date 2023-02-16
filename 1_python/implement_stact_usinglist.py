l=[]
while True:
    c=int(input(''' 
    1 Push Elements
    2 POP Elements
    3 Peek Element
    4 Display Elements
    5 Exit

    '''))

    if c==1:
        n=input("enter the value :- ")
        l.append(n)
        print(l)

    elif c==2:
        if len(l)==0:
            print("empty Stack")
        else:
          p=l.pop()
          print(p)
          print(l)

    elif c==3:
        if len(l)==0:
            print("empty Stack")
        else:
            print("last stack elemant :- ",l[-1])
    
    elif c==4:
        print("display Stack :- "+ str(l))

    elif c==5:
        break
    else:
        print("please enter valid operation")
 



