"""singular to plural"""

word=input()

lt1=["s","x"]
lt2=["a","e","i","o","u"]

if word[-1] in lt1:
    ans=word+"es"
elif word[-2::1]=="ch":
    ans=word+"es"
elif word[-1]=="y" and word[-2] not in lt2:
    ans=word[:-1]+"ies"
else:
    ans=word+"s"

print(ans)
