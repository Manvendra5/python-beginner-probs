num=int(input("enter any number : "))
d=[]
for x in range(1,num+1):
    if num%x==0:
        temp=x
        d.append(temp)
print(d)        