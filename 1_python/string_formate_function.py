#named index
a='hello {fname} {lname}'.format(fname='adarsh',lname='rai')

#number index
b='hello {0} {1}'.format('adarsh','rai')

#empty placeholder
c='hello {} {} {}'.format('adarsh','rai','0305')

d='adarsh {a}{b}'.format(a=200,b=3)



print(a)
print(b)
print(c)
print(d)