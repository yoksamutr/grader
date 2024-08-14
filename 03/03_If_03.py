"""gymnastic score"""

lscore=[float(i) for i in input().split()]
sum_score=sum(lscore)-max(lscore)-min(lscore)
print(round(sum_score/2,2))
