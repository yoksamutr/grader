"""change of major"""

s1=input().split()
s2=input().split()
grade={"A":4,"B":3,"C":2,"D":1,"F":0}

def check(comp,cal1,cal2):
    if(comp==4 and cal1>=2 and cal2 >=2):
        return True
    return False
    
pass1=check(grade[s1[2]],grade[s1[3]],grade[s1[4]])
pass2=check(grade[s2[2]],grade[s2[3]],grade[s2[4]])
gpax1=float(s1[1])
gpax2=float(s2[1])

if pass1 and pass2:
    if gpax1>gpax2:
        print(s1[0])
    elif gpax1<gpax2:
        print(s2[0])
    else:
        cal11=grade[s1[3]]
        cal12=grade[s2[3]]
        if cal11>cal12:
            print(s1[0])
        elif cal11<cal12:
            print(s2[0])
        else:
            cal21=grade[s1[4]]
            cal22=grade[s2[4]]
            if cal21>cal22:
                print(s1[0])
            elif cal21<cal22:
                print(s2[0])
            else:
                print("Both")
elif pass1:
    print(s1[0])
elif pass2:
    print(s2[0])
else:
    print("None")
