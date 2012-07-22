import random
import string
import qGen2Support
from quesSupport import *
from dataSets import *

chapter = 2

qq = Question(100)
qq.title = "If Statements"
def qqq(n,me):
	op = random.randrange(0,6)
	n1 = random.randrange(-50,200,5)
	val1 = random.choice(['good', 'ok', 'yes', 'in spec'])
	val2 = random.choice(['bad', 'poor', 'no', 'out of spec'])
	xVals = [-99999,n1-1,n1,n1+1,99999]  # Values for testing
	
	q = "Write a Python 'if' statement that sets the variable 'result' to '"+val1+"'\nif 'x' is "
	
	a = 'result = "'+val2+'"\nif x % '+str(n1)+':\n    result = "'+val1+'"\n\n  or as\n\n'+\
	    'if x % '+str(n1)+':\n    result = "'+val1+'"\nelse:\n    result = "'+val2+'"'
	
	if op == 0: # ==
		q += "equal to "+str(n1)
		resultVals = [val2,val2,val1,val2,val2] # Correct result values
		a=a.replace('%','==')
	if op == 1: # !=
		q += "not equal to "+str(n1)
		resultVals = [val1,val1,val2,val1,val1] # Correct result values
		a=a.replace('%','!=')
	if op == 2: # <
		q += "less than "+str(n1)
		resultVals = [val1,val1,val2,val2,val2] # Correct result values
		a=a.replace('%','<')
	if op == 3: # <=
		q += "less than or equal to "+str(n1)
		resultVals = [val1,val1,val1,val2,val2] # Correct result values
		a=a.replace('%','<=')
	if op == 4: # >
		q += "greater than "+str(n1)
		resultVals = [val2,val2,val2,val1,val1] # Correct result values
		a=a.replace('%','>')
	if op == 5: # >=
		q += "greater than or equal to "+str(n1)
		resultVals = [val2,val2,val1,val1,val1] # Correct result values
		a=a.replace('%','>=')

	q += " and to '"+val2+"' otherwise.\nThis can be done without using 'else'."
	
	me.setupCode = "    __ans=[]\n    for x in "+str(xVals)+":\n"

	me.innerCheckCode = "        if 'result' in locals():__ans.append(result)\n"

	me.outerCheckCode = """\
if 'result' not in ld:
    print 'result not found.'
    sys.exit()
if __ans != """+str(resultVals)+""":
    print 'Incorrect answer(s).'
    print 'for data values: """+str(xVals)+''' the expected results are:'
    print "'''+str(resultVals)+""" but your results were:"
    print str(__ans)
    sys.exit()
if len(ld) > 2:
    print 'Unneeded variable used.'
    sys.exit()"""
	
	return q,a    	
qq.genQFunc=qqq	
	


qq = Question(3)
qq.title = "While Statements"
def qqq(n,me):
	mul = n+2
	start = random.randrange(5,15)
	x = random.randrange(4)
	ans = start
	for i in range(x):
	    ans *= mul
	xVals = [0,ans-1,ans,ans+1]  # Values for testing
	resultVals = []
	for val in xVals:
	    xx = start
	    while xx <= val:
	        xx *= mul
	    resultVals.append(xx)  # answers using 'start' and 'highVal's from xVals
	    
	word = "*** bad value ***"
	if mul == 2: word = "doubles"
	if mul == 3: word = "triples"
	if mul == 4: word = "quadruples"
	q  = "Use a 'while' loop that repeatedly "+word+" the value stored in\n"
	q += "'start'.  If the result is greater than 'highVal' stop looping\n"
	q += "and return the computed value as 'big', otherwise continue\n"
	q += "looping.  Do not change the value of either 'start' or 'highVal'."
	
	a = 'big = start\nwhile big <= highVal:\n    big *= '+str(mul)+'\n'
    
	me.setupCode  = "    start = "+str(start)+"\n    __check=[]\n"
	me.setupCode += "    __ans=[]\n    for highVal in "+str(xVals)+":\n"

	me.innerCheckCode  = "        if 'big' in locals():__ans.append(big)\n"
	me.innerCheckCode += "        __check.append(highVal)\n"

	me.outerCheckCode = """\
if 'big' not in ld:
    print 'big not found.'
    sys.exit()
if __ans != """+str(resultVals)+""":
    print 'Incorrect answer(s).  Using start = """+str(start)+""" and testing'
    print 'for highVal values: """+str(xVals)+''' the expected results are:'
    print "'''+str(resultVals)+""" but your results were:"
    print str(__ans)
    sys.exit()
if start != """+str(start)+""":
    print 'The value of start has changed'
    sys.exit()
if __check != """+str(xVals)+""":
    print 'the value of highVal has changed'
    sys.exit()
if len(ld) > 3:
    print 'Unneeded variable used.'
    sys.exit()"""

	
	return q,a    	
qq.genQFunc=qqq	
	


qq = Question(1)
qq.title = "For Statements: Count and Sum"
def qqq(n,me):
	size = random.randrange(6)+5
	lis = []
	for i in range(size):
		if random.random()>.6:
			lis.append(qGen2Support.randStr(3,8))
		else:
			lis.append(str(random.randrange(50,99999)))
	count = 0
	sum = 0
	for s in lis:
	    if s.isdigit(): 
	        count += 1
	        sum += int(s)
		
	q  = "Use a 'for' loop to examine the strings in the list 'myList'.\n"
	q += "Determine how many of the strings appear to be integers and\n"
	q += "set the variable 'count' to refer to that value.\n"
	q += "Also, compute the sum of these values and call that 'sumOfInts'."
	
	a = 'count = 0\nsum = 0\nfor stng in myList:\n    if stng.isdigit():\n'+\
	    '        count += 1\n        sum += int(stng)\n'
    
	me.setupCode  = "        myList = "+str(lis)+"\n"

	me.outerCheckCode = """\
import re
if 'count' not in ld:
    print 'count not found.'
    sys.exit()
if 'sumOfInts' not in ld:
    print 'sumOfInts not found.'
    sys.exit()
if not re.search("\\n\s*for\s[a-zA-Z0-9_]+\sin\s[a-zA-Z0-9_]+:",__code_):
    print "does not use a 'for' loop."
    sys.exit()
if count != """+str(count)+""":
    print 'Incorrect answer.  The given list to test was:'
    print '''"""+str(lis)+"""'''
    print 'The number of strings that appear to be integers is """+str(count)+"""'
    print 'But your result was',count
    sys.exit()
if sumOfInts != """+str(sum)+""":
    print 'Incorrect answer.  The given list to test was:'
    print '''"""+str(lis)+"""'''
    print 'The sum of the strings that appear to be integers is """+str(sum)+"""'
    print 'But your result was',sumOfInts
    sys.exit()
if myList != """+str(lis)+""":
    print 'The contents of myList has changed'
    sys.exit()
if len(ld) > 4:
    print 'Unneeded variable used.'
    sys.exit()"""

	
	return q,a    	
qq.genQFunc=qqq	


qq = Question(1)
qq.title = "For Statements: Concatenate"
def qqq(n,me):
	size = random.randrange(6)+3
	lis = []
	for i in range(size):
		lis.append(qGen2Support.randStr(3,8))
	all = ""
	for s in lis:
	    all += s
		
	q  = "Use a 'for' loop to concatenate the strings in the list 'myList'.\n"
	q += "Name the concatenated string 'all'.\n"
	
	a = 'all = ""\nfor stng in myList:\n    all += stng\n'
    
	me.setupCode  = "        myList = "+str(lis)+"\n"

	me.outerCheckCode = """\
import re
if 'all' not in ld:
    print 'all not found.'
    sys.exit()
if not re.search("\\n\s*for\s[a-zA-Z0-9_]+\sin\s[a-zA-Z0-9_]+:",__code_):
    print "does not use a 'for' loop."
    sys.exit()
if all != '"""+str(all)+"""':
    print 'Incorrect answer.  The given list to test was:'
    print '''"""+str(lis)+"""'''
    print 'The concatenated result should be """+str(all)+"""'
    print 'But your result was',all
    sys.exit()
if myList != """+str(lis)+""":
    print 'The contents of myList has changed'
    sys.exit()
if len(ld) > 3:
    print 'Unneeded variable used.'
    sys.exit()"""

	
	return q,a    	
qq.genQFunc=qqq	
	
	
