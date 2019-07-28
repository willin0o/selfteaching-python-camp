'''
s =range(1,10)
#n =range(1,x+1)
#n=i+(i+1)
for x in s:
    for y in range(1,x+1):
        print(x,"*",y,"=",x*y,end='\t')
    print()
'''
x=1
while x < 10:
    if x % 2==0:
        print()
    else:
        for y in range(1,x+1):
            print(x,"*",y,"=",x*y,end='\t')
    x+=1
