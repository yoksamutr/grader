"""rotate string"""

order=str(input())
n=int(input())

invalid=False
lt=[]
ip=str(input())
l=len(ip)
lt.append(ip)

for i in range(n-1):
    ip=str(input())
    if len(ip)!=l:
        invalid=True
    lt.append(ip)
      
def order90(lt1):
    for i1 in range(l):
        for j1 in range(len(lt1)-1,-1,-1):
            print(lt1[j1][i1],end="")
        print("")

def order180(lt2):
    for i2 in range(len(lt2)-1,-1,-1):
        for j2 in range(l-1,-1,-1):
            print(lt2[i2][j2],end="")
        print("")
            
def orderflip(lt3):
    for i3 in range(len(lt3)):
        for j3 in range(l-1,-1,-1):
            print(lt3[i3][j3],end="")
        print("")
    
if invalid:
    print("Invalid size")
else:
    if order=="90":
        order90(lt)
    elif order=="180":
        order180(lt)
    else:
        orderflip(lt)
