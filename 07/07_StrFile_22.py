"""anagram"""

word1=input()
word2=input()

def check(w1,w2):
    lt1=[]
    lt2=[]
    for i in w1:
        if i!=" ":
            lt1.append(i.lower())
    for j in w2:
        if j!=" ":
            lt2.append(j.lower())
    if sorted(lt1)==sorted(lt2):
        print("YES")
    else:
        print("NO")

check(word1,word2)
