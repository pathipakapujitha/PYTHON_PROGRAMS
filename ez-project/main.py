#'rock','paper','scissor' game
from random import randint
#n=int(input("enter no of times game should be played: "))
pc=0
cc=0
limit=5
while True:
    choice=['rock','paper','scissor']
    player=input(f"choose from {choice}").lower()
    comp=choice[randint(0,2)]
    print("computer choses",comp)
    if player == comp :
        print("draw match")
    elif player == "paper" and comp == "rock":
        #print("player win")
        pc=pc+1
    elif player == "paper" and comp == "rock":
        #print("player win")
        pc=pc+1
    elif player == "paper" and comp == "rock":
        #print("player win")
        pc=pc+1
    else:
        #print("computer wins")
        cc=cc+1
    if pc==limit or cc==limit:
        break
print("player score: ",pc,"computer score: ",cc)
if pc==limit :
    print("player wins")
elif cc==limit:
    print("computer wins")