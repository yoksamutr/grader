"""cash"""

def total(pocket):
    val=0
    for key in pocket:
        val+=key*pocket[key]
    return val

def take(pocket,money_in):
    for key in money_in:
        if key in pocket:
            pocket[key]+=money_in[key]
        else:
            pocket[key]=money_in[key]
    return pocket

def pay(pocket,amt):
    money_out={}
    for val in sorted(pocket.keys())[::-1]:
        cnt=min(pocket[val],amt//val)
        money_out[val]=cnt
        pocket[val]-=cnt
        amt-=val*cnt
        if money_out[val]==0:
            money_out.pop(val)
    if amt>0:
        take(pocket,money_out)
        return {}
    else:
        return money_out
                
exec(input().strip())
