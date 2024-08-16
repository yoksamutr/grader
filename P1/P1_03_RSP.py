"""rock scissor paper"""

m=int(input())

dic={"R":"S","S":"P","P":"R"} #win:lose

p1=0; p2=0
for i in range(3*m):
    t1,t2=[str(e) for e in input().split()]
    if dic[t1]==t2:
        p1+=1
    if dic[t2]==t1:
        p2+=1
    if p1==m or p2==m:
        break

print(p1,p2)

if p1>p2:
    print("Player 1 wins")
elif p1<p2:
    print("Player 2 wins")
else:
    print("Tie")
