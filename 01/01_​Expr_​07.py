"""body surface area (function)"""

def mosteller(w,h):
    mos=((w*h)**0.5)/60
    return mos

def du_bois(w,h):
    du=0.007184*(w**0.425)*(h**0.725)
    return du

def fujimoto(w,h):
    fuji=0.008883*(w**0.444)*(h**0.663)
    return fuji

def main():
    w=float(input())
    h=float(input())
    mos=mosteller(w,h)
    du=du_bois(w,h)
    fuji=fujimoto(w,h)
    print("Mosteller =", round(mos, 5))
    print("Du Bois =", round(du, 5))
    print("Fujimoto =", round(fuji,5))
    
exec(input())
