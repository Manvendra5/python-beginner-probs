strin=input()
strin1=strin.split()
strin2=[]
x=len(strin1)-1
while x>=0:
    temp=strin1[x]
    strin2.append(temp)
    x=x-1
for i in strin2:
    print(i,end=" ")
