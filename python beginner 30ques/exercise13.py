temp=0
i=1
l=[]
siz=int(input("size of list :"))
if siz>=2:
    l=[1,1]
    while i<siz-1:
        l.append(l[i]+l[i-1])
        i=i+1
print(l)        

    
