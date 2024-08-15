"""change of major (function)"""

def check(comp,cal1,cal2):
    if(comp==4 and cal1>=2 and cal2>=2):
        return True
    return False

def choose(s1,s2):
    id1,gp1,cp1,cal11,cal21=s1
    id2,gp2,cp2,cal12,cal22=s2
    grade={"A":4,"B":3,"C":2,"D":1,"F":0}
    pass1=check(grade[cp1],grade[cal11],grade[cal21])
    pass2=check(grade[cp2],grade[cal12],grade[cal22])
    gp1=float(gp1)
    gp2=float(gp2)
    
    if pass1 and pass2:
        if gp1>gp2:
            return [id1]
        elif gp1<gp2:
            return [id2]
        else:
            cal11=grade[cal11]
            cal12=grade[cal12]
            if cal11>cal12:
                return [id1]
            elif cal11<cal12:
                return [id2]
            else:
                cal21=grade[cal21]
                cal22=grade[cal22]
                if cal21>cal22:
                    return [id1]
                elif cal21<cal22:
                    return [id2]
                else:
                    return [id1,id2]
    elif pass1:
        return [id1]
    elif pass2:
        return [id2]
    else:
        return []
        
exec(input())
