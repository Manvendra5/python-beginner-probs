size=int(input("size of array:  "))
a=[]
for i in range(size):
    temp=int(input("enter element  "))
    a.append(temp)
print(a)   
x=0
while x<size:
        while a[x]>5:
                if a[x]>5:
                        del a[x]
                        size=size-1      
        x=x+1
print(a)
