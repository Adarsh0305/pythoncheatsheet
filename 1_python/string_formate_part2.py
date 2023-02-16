a='hello {a:10}{b}'.format(a=200,b=3)
print(a)               # here a:10 means a 10 char ka sapce choda pr a me 3 number hai 
                        # isliye a me 7 char ka space chada or baki ka print kiya

b=a='hello {a:^10}{b}'.format(a=200,b=3)
print(b)                                    # ^ is sign se 200 bich me print hoga

c='hello {a:<10}{b}'.format(a=200,b=3)
print(c)                                    # < is sign se 200 left me print hoga


d=a='hello {a:>10}{b}'.format(a=200,b=3)
print(d)