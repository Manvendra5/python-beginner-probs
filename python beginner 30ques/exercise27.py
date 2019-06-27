a=[[0,0,0],[0,0,0],[0,0,0]]
def entrx():
    if a[row][col]==0:
        a[row][col]='x'
    else :
        print("already occupied choose another position :")
        move()
    y=input("(start/continue)//stop y/n:")
    if y=='y':
        move()
    if y=='n':
        print(a)    
def entro():
    if a[row][col]==0:
        a[row][col]='o'
    else :
        print("already occupied choose another position :")
        move()
    y=input("(start/continue)//stop y/n:")
    if y=='y':
        move()
    if y=='n':
        print(a)       
def move():
    global row,col
    row=int(input("entr the row no. :"))
    col=int(input("entr the column no. :"))
    z=input("choice x/o :")
    if z=='x':
        entrx()
    elif z=='o':
        entro()            
y=input("(start/continue)//stop y/n:")
if y=='y':
    move()
if y=='n':
    print(a)







