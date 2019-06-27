import random
i=0 
cows=0
bulls=0
def inp():
    global rndm,user,rndm1 
    rndm=random.randint(1000,9999)
    rndm1=str(rndm)
    user=input("enter any 4 digit no.:")
    print(rndm1)
    check()
def check():
    global i,cows,bulls
    i=0
    cows=0
    bulls=0
    while i<4:
        if rndm1[i]==user[i]:
            cows =cows+1
        else:
            bulls=bulls+1
        i=i+1
    print("cows:",cows)
    print("bulls:",bulls) 
    if cows!=4:
        inp()
    elif cows==4:
        exit()     
inp()    
      
