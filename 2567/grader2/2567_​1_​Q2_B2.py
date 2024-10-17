"""text search"""

word=input().lower()
n=int(input())

lt=[input() for _ in range(n)]
ans="\n".join(lt)
copy=ans.lower().replace("\n"," ")

x=copy.find(word)
while x!=-1:
    ans=ans[:x]+"<found>"+ans[x:x+len(word)]+"</found>"+ans[x+len(word):]
    copy=ans.lower().replace("\n"," ")
    x=copy.find(word,x+len(word)+15)

print(ans)
