import random
def user():
    global num,rndm,x
    rndm=random.randint(1,9)
    num=int(input("enter any no. btw [1,9]"))
    check()
    x=input("wanna play again y/n:")
    if x=='y':
        user()
    elif x=='n':
         print("---------thank you for playing---------- ")
         exit()
def check():
    if num==rndm:
        print("right guess.")
    elif num<rndm:
        print("number less than random no.")
    elif num>rndm:
        print("number greater than random no.")    
user()
        
        


