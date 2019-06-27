import random 
l1=[]
l2=[]
sz1=int(input("enter size of list1:"))
sz2=int(input("enter size of list2:"))
for i in range(0,sz1):
    temp1=random.randint(0,100)
    l1.append(temp1)
for i in range(0,sz2):
    temp1=random.randint(0,100)
    l2.append(temp1) 
print(l1)
print(l2)    
set1=set(l1)
set2=set(l2)
print(list(set1&set2))

