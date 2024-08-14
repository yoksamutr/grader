"""mobile number"""

ipt=str(input())
check=ipt[0:2]

if check=="06" or check=="08" or check=="09":
    print("Mobile number")
else:
    print("Not a mobile number")
