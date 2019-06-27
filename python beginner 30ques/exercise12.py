import random
l=[]
l1=[]
siz=int(input("enter the size of list :"))
def take():
    global l,temp
    for i in range(siz):
        temp=random.randint(0,100)
        l.append(temp)
def new():
    global l1,temp1
    temp1=l[0]
    l1.append(temp1)
    temp1=l[siz-1]
    l1.append(temp1)
    print(l1)
take()
print(l)
new()    