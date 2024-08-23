"""next prime"""

def is_prime(n):
    if n<=1:
        return False
    for k in range(2,int(n**0.5)+1):
        if n%k==0:
            return False
    return True

def next_prime(n):
    ans=0
    while True:
        n+=1
        if is_prime(n):
            ans=n
            break
    return ans

def next_twin_prime(n):
    ans1,ans2=0,0
    while True:
        n+=1
        if is_prime(n) and is_prime(n+2):
            ans1=n
            ans2=n+2
            break
    return (ans1,ans2)

exec(input().strip())
