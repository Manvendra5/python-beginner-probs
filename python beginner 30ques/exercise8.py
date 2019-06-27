p1score=0
p2score=0
def game(p1,p2):
    
    if p1=="rock" and p2=="scissors":
        p1score=p1score+1
    elif p2=="rock" and p1=="scissors":
        p2score=p2score+1
    elif p2=="paper" and p1=="scissors":
        p1score=p1score+1
    elif p1=="paper" and p2=="scissors":
        p2score=p2score+1
    elif p2=="rock" and p1=="paper":
        p1score=p1score+1
    elif p2=="rock" and p1=="paper":
        p2score=p2score+1
p11=input("player 1 :")
p22=input("player 2 :")
game(p11,p22)

print("Scoreboard:   p1", p1score ,":", p2score ,  "p2")
YN=input("wanna play again ? enter yes or no")
if YN=='y':
    p11=input("player 1 :")
    p22=input("player 2 :")
    game(p11,p22)
else:
    end        
