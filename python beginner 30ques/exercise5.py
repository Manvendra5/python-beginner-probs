s1=int(input("enter s1: "))
s2=int(input("enter s2 : "))
l1=[]
l2=[]
fl=[]
j=0
count=0
for x in range(s1):
    temp1=int(input("enter l1: "))
    l1.append(temp1) 
for y in range(s2):    
    temp2=int(input("enter l2: "))
    l2.append(temp2) 
for i in range(s1):
    while l1[i]==l2[j]: 
        count=count+1 
        j=j+1  
    if count!=0: 
        fl.append(l1[i]) 
    count=0         
print(fl)     