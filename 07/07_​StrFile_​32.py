"""password strength"""

def less8(p):
    if len(p)<8:
        return True
    return False

def no_lowercase(p):
    if p==p.upper():
        return True
    return False

def no_uppercase(p):
    if p==p.lower():
        return True
    return False
    
def no_number(p):
    flag=True
    for i in p:
        if "0"<=i<="9":
            flag=False
            break
    if flag:
        return True
    return False
        
def no_symbols(p):
    flag=True
    for i in p:
        if i in "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
            flag=False
            break
    if flag:
        return True
    return False
        
def repetition(p):
    for i in range(len(p)-3):
        if p[i]*4==p[i:i+4]:
            return True
    return False
        
def isdigit(p):
    for i in p:
        if not "0"<=i<="9":
            return False
    return True

def number_sequence(p):
    lnum="01234567890123456789"
    rnum=lnum[-1::-1]
    for i in range(len(p)-3):
        num=p[i:i+4]
        if isdigit(num):
            if num in lnum or num in rnum:
                return True
    return False
            
def letter_sequence(p):
    abc="abcdefghijklmnopqrstuvwxyz"
    cba=abc[-1::-1]
    for i in range(len(p)-3):
        str1=p[i:i+4].lower()
        if str1 in abc or str1 in cba:
            return True
    return False
        
def keyboard(p):
    r1="!@#$%^&*()_+"
    r2="qwertyuiop"
    r3="asdfghjkl"
    r4="zxcvbnm"
    for i in range(len(p)-3):
        str1=p[i:i+4].lower()
        if str1 in r1 or str1 in r1[-1::-1]:
            return True
        elif str1 in r2 or str1 in r2[-1::-1]:
            return True
        elif str1 in r3 or str1 in r3[-1::-1]:
            return True
        elif str1 in r4 or str1 in r4[-1::-1]:
            return True
    return False

password=input()
flag=True

if less8(password):
    print("Less than 8 characters")
    flag=False
if no_lowercase(password):
    print("No lowercase letters")
    flag=False
if no_uppercase(password):
    print("No uppercase letters")
    flag=False
if no_number(password):
    print("No numbers")
    flag=False
if no_symbols(password):
    print("No symbols")
    flag=False
if repetition(password):
    print("Character repetition")
    flag=False
if number_sequence(password):
    print("Number sequence")
    flag=False
if letter_sequence(password):
    print("Letter sequence")
    flag=False
if keyboard(password):
    print("Keyboard pattern")
    flag=False
if flag:
    print("OK")
