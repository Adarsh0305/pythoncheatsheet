# create nasted Dictionary
course={
  'bsc':{'durection':'3 year','fees':'8000'},
   'Engineering':{'durection':'4 year','fees':'4 lakh 80 thousand'},
   'MBBS':{'durection':'5 year',"fees":'1 Cr'}
}
print(course)
print()
print(course['bsc'])
print()
print(course['Engineering']['durection'])# yaha engineering ke andar ki dic ko print karega
print()
print(course['bsc'])
print()
print(course['bsc']['fees'])
print()

# print multiple data 
for i,n in course.items():    # item key and value ko alag karta hai
    print(i,n)
print()

for k,v in course.items():
    print(k,v['durection'],v['fees'])     # only print duriction and fees
print()

# how to update in dictionary
course['bsc']['fees']=10000        # 8000 updated to 10000 
for j,k in course.items():
    print(j,k)
print()

del course['bsc']['fees']      # fees is delected 
for o,p in course.items():
    print(o,p)