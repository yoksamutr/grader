"""thai numerals"""

def to_Thai(n):
    thai={1:"neung",2:"song",3:"sam",
      4:"si",5:"ha",6:"hok",7:"chet",
      8:"paet",9:"kao",10:"sip"}
    n=int(n)
    out=[]
    if n==0:
        out.append("soon")
    if n==1:
        out.append("neung")
        n=0
    if n>=1000:
        out.append(thai[n//1000])
        out.append("pun")
        n%=1000
    if n>=100:
        out.append(thai[n//100])
        out.append("roi")
        n%=100
    thai[2]="yi"
    if n>=20:
        out.append(thai[n//10])
        out.append("sip")
    thai[2]="song"
    if 10<=n<=19:
        out.append("sip")
    n%=10
    thai[1]="et"
    if n>0:
        out.append(thai[n])
    return " ".join(out)

exec(input().strip())
