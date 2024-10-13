"""Anagram II"""

w1=input()
w2=input()

def mp(w):
    m={}
    for i in w.lower():
        if "a"<=i<="z":
            if i in m:
                m[i]+=1
            else:
                m[i]=1
    return dict(sorted(m.items()))

mp1,mp2=mp(w1),mp(w2)

def to_ans(d1,d2,w):
    ans=[]
    for x in d1:
        if x in d2:
            diff=d1[x]-d2[x]
            if diff==1:
                ans.append(" ".join([" - remove",str(1),x]))
            elif diff>1:
                ans.append(" ".join([" - remove",str(diff),x+"'s"]))
        elif d1[x]==1:
            ans.append(" ".join([" - remove",str(1),x]))
        elif d1[x]>1:
            ans.append(" ".join([" - remove",str(d1[x]),x+"'s"]))
    if len(ans)==0:
        return [w," - None"]
    return [w]+ans

for k in to_ans(mp1,mp2,w1):
    print(k)
for l in to_ans(mp2,mp1,w2):
    print(l)
