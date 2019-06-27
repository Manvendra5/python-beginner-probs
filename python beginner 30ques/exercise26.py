n = int(input()) 
a = []
p1=0
p2=0
for i in range(n):
    a.append([int(j) for j in input().split()])
for i in range(3):
    if a[i][0]==a[i][1]==a[i][2]==1:
        p1=p1+1
    elif a[i][0]==a[i][1]==a[i][2]==2:
        p2=p2+1
for i in range(3):
    if a[0][i]==a[1][i]==a[2][i]==1:
        p1=p1+1
    elif a[0][i]==a[1][i]==a[2][i]==2:
        p2=p2+1  
if a[0][0]==a[1][1]==a[2][2]==1:
    p1=p1+1
elif a[0][0]==a[1][1]==a[2][2]==2:
    p2=p2+1
if a[0][2]==a[1][1]==a[2][1]==1:
    p1=p1+1
elif a[0][2]==a[1][1]==a[2][1]==2:
    p2=p2+1
print("p1:",p1)
print("p2:",p2)

    



