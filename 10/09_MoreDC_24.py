"""Cartoons"""

dct={}
while True:
    ip=input()
    if ip=="q":
        break
    name,animal=ip.split(", ")
    if animal not in dct:
        dct[animal]=[name]
    else:
        dct[animal].append(name)

for key,val in dct.items():
    print(key+":",", ".join(val))
