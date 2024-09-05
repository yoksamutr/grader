"""anagram II"""

str1=input()
str2=input()
            
def to_dict(word):
    dct={}
    for i in word:
        i=i.lower()
        if "a"<=i<="z":
            if i not in dct:
                dct[i]=1
            else:
                dct[i]+=1
    dct=dict(sorted(dct.items()))
    return dct #return dict

dct1,dct2=to_dict(str1),to_dict(str2)

def to_ans(l1,l2): #dict,dict
    ans=[]
    for x in l1:
        if x in l2:
            diff=l1[x]-l2[x]
            if diff==1:
                ans.append([" - remove",str(diff),x])
            elif diff>1:
                ans.append([" - remove",str(diff),x+"'s"])
        elif l1[x]==1:
            ans.append([" - remove",str(l1[x]),x])
        else:
            ans.append([" - remove",str(l1[x]),x+"'s"])
    return ans

ans1,ans2=to_ans(dct1,dct2),to_ans(dct2,dct1)

def print_ans(word,lst):
    print(word)
    if len(lst)==0:
        print(" - None")
    else:
        for m in lst:
            print(" ".join(m))

print_ans(str1,ans1)
print_ans(str2,ans2)
