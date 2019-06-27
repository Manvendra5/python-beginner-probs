l=[]
temp=0
i=0
def largest():
    global l,temp,i
    print("entr any three numbers :")
    for i in range(3):
        temp=int(input("entr the no. :"))
        l.append(temp)
    l.sort()
    print("largest no. is : ",l[2])
largest()        
