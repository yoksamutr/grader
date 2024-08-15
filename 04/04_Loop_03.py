"""MCQ"""

answer=str(input())
ans=str(input())

if len(answer)!=len(ans):
    print("Incomplete answer")
else:
    count=0
    for i in range(len(ans)):
        if answer[i]==ans[i]:
            count+=1
    print(count)
