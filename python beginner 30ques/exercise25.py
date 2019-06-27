import random
count=0
rndm=random.randint(0,100)
def check():
    global rndm,user,count
    user=int(input("entr  :"))
    print(rndm)
    if user==rndm:
        count=count+1
        print("no. of guesses reguired:",count)
    elif user!=rndm:
        count=count+1
        check()    
check()        





