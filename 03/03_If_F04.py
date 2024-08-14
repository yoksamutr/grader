"""mobile number (function)"""

def is_mobile_number(number):
    check=str(number)[0:2]
    if (check=="06" or check=="08" or check=="09") and len(str(number))==10:
        return True
    return False

exec(input())
