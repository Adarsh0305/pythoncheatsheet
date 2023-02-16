l=[]
while True:
    c=int(input(''' 
    1 Push Elements
    2 POP First Elements
    3 Front/First Element
    4 Rear/Last Elements
    5 Display Queue
    6 Exit

    '''))

    if c==1:
        n=input("enter the value :- ")
        l.append(n)
        print(l)

    elif c==2:
        if len(l)==0:
            print("empty Queue")
        else:
            del l[0]
            print(l)

    elif c==3:
        if len(l)==0:
            print("empty Queue")
        else:
            print("First Queue elemant :- ",l[0])
    
    elif c==4:
         if len(l)==0:
            print("empty queue")
        else:
             print("Last Queue Element :-",l[-1])

    elif c==5:
       print("display Queue :- "+str(l) )

    elif c==6:
        break
    else:
        print("please enter valid operation")
 



