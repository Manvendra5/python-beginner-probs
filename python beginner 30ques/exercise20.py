siz=int(input("enter the size of array:"))
temp=0
l=[]
i=0
high=siz-1
low=0
mid=int((low+high)/2) 
for i in range(siz):
    temp=int(input("enter :"))
    l.append(temp) 
l.sort()
user=int(input("search :"))
def sorrt(x,y):
    global mid,high,low,user
    low=x
    high=y 
    mid=int((high+low)/2)
    if low<high:
        if user==l[mid]:
            print("index:",mid)
            exit()
        elif l[mid]>user:
            low=mid+1
        elif l[mid]<user:
            high=mid-1    
    sorrt(low,high)
sorrt(low,high) 
