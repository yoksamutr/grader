"""average"""

lt=[]
while True:
    n=input()
    if n=="q":
        break
    lt.append(float(n))

if len(lt)==0:
    print("No Data")
else:
    ans=sum(lt)/len(lt)
    print(round(ans,2))
