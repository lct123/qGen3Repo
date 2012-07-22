# qGen2Support.py

import random
import string

def fpTruncate(val,places):
    if val >= 0.1:
        template = "%"+str(places)+"f"
        x = template % (val)
        while True:
            if x[-1] == '0':
                x = x[:-1]
            else:
                return x
    else:
        template = "%."+str(places-1)+"e"
        x = template % (val)
        while True:
            if '0e' in x and not '.0e' in x:
                x = x.replace('0e','e')
            else:
                return x
			
def pad80(s):
    spl = string.split(s,'\n')
    for i in range(len(spl)):
        spl[i] = string.ljust(spl[i],80)
    return string.join(spl,'\n')    
    

def toBinary(value, numDigits=16, spacing=99):
    result = ""
    count = spacing
    if numDigits:
        for i in range(numDigits):
            if value%2:
                result = "1" + result
            else:
                result = "0" + result
            count -= 1
            if not count:
                result = " " + result
                count = spacing
            value /= 2
    else:
        while value:
            if value%2:
                result = "1" + result
            else:
                result = "0" + result
            count -= 1
            if not count:
                result = " " + result
                count = spacing
            value /= 2
        if not result: result = "0"
    if result[0] == " ": result = result[1:]
    return result

def fromBinary(binString):
    ans = 0
    for ch in binString:
        if ch == "0":
            ans *= 2
        elif ch == "1":
            ans *= 2
            ans += 1
        else:
            print "ERROR in qGenSupport.fromBinary"
    return ans

def rand4(seed=None):
    if not seed:
        random.seed()
        seed = random.randint(1000,9999)
    random.seed(seed)
    return seed
        
def randStr(minLen,maxLen):
	s = ""
	for i in range(random.randint(minLen,maxLen)):
	    s += chr(random.randint(33,126))
	return s