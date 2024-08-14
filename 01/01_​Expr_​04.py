import math

a=float(input())
b=float(input())
mos=(math.sqrt(a*b))/60
hay=0.024265*pow(a,0.5378)*pow(b,0.3964)
boy=0.0333*pow(a,(0.6157-(0.0188*math.log10(a))))*pow(b,0.3)
print(mos)
print(hay)
print(boy)
