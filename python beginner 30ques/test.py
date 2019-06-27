t=int(input())
for i in range(t):
    l=[]
    j=10
    n=int(input())
    for j in range(10,1000):
        sum=0
        j=str(j)
        j=list(j)
        x=len(j)
        z=0
        for z in range(x):
            if j[z]!='.':
                sum=sum+int(j[z])     
        j=str(j)           
        if sum==10:
            l.append(j) 
    print(l[n]) 
