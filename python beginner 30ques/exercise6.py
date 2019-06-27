st=input("enter the string : ")
y=-1
count=0
for x in range(len(st)):
    if st[x]==st[y]:
        count=count+1
    y=y-1
if count==len(st):
    print("palindrome")
else:
    print("not a palindrome")            