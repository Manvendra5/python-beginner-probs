num=int(input("enter any no.:"))
i=2
flag=False
def check():
    global i
    global flag
    while i<num:
        if(num%i==0):
            flag=True
            break
        i=i+1
check()        
if flag:
    print("not a prime no.")
else:
    print("prime no.")             
