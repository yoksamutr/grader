"""six-red snooker score"""

colors={"R":1,"Y":2,"G":3,"W":4,
        "B":5,"P":6,"K":7,"X":0}
player={"1":0,"2":0}

red=6
other=6
while red>0:
    ip=input()
    if ip[1]!="X":
        player[ip[0]]+=1+colors[ip[2]]
        red-=1
while other>0:
    ipt=input()
    if ipt[1]!="X":
        player[ipt[0]]+=colors[ipt[1]]
        other-=1

print(player["1"],player["2"])
if player["1"]>player["2"]:
    print("Player 1 wins")
elif player["1"]<player["2"]:
    print("Player 2 wins")
else:
    print("Tie")
