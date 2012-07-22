import random
import string
import qGen2Support
from quesSupport import *
from dataSets import *

chapter = 4

qq = Question(6)
qq.title = "String Indexing"
def qqq(n,me):
	pos = random.choice([(0,'first'), 
						 (1,'second'), 
						 (2,'third'),
						 (-1,'last'), 
						 (-2,'second last'), 
						 (-3,'third last')])
						 
	xVals = []
	for i in range(5):
		xVals.append(qGen2Support.randStr(5,9))
	
	
	q  = "Write a Python statement that sets the variable 'result' to \n"
	q += "the "+pos[1]+" character of the string 'myString'\n"

	resultVals = []
	for v in xVals:
		resultVals.append(v[pos[0]])

	a = 'result = myString['+str(pos[0])+']\n'
	
	me.setupCode = "    __ans=[]\n    for myString in "+str(xVals)+":\n"

	me.innerCheckCode = "        if 'result' in locals():__ans.append(result)\n"

	me.outerCheckCode = """\
if 'result' not in ld:
    print 'result not found.'
    sys.exit()
if __ans != """+str(resultVals)+""":
    print 'Incorrect answer(s).'
    print '''for data values: """+str(xVals)+""" the expected results are:'''
    print '''"""+str(resultVals)+""" but your results were:'''
    print str(__ans)
    sys.exit()
if len(ld) > 2:
    print 'Unneeded variable used.'
    sys.exit()"""
	
	return q,a    	
qq.genQFunc=qqq	
	


qq = Question(18)
qq.title = "String Slicing"
def qqq(n,me):
	starts = [(':','first'), 
			  ('1:','second'), 
			  ('2:','third')]
	ends =   [('4','fourth'), 
			  ('5','fifth'), 
			  ('6','sixth'),
			  ('','last'),
			  ('-1','second last'),
			  ('-2','third last')]
	x = random.randrange(18)
	startPos = starts[x/6]
	endPos = ends[x%6]
	
	xVals = []
	for i in range(3):
		xVals.append(qGen2Support.randStr(10,14))
	
	
	q  = "Write a Python statement that sets the variable 'result' to the\n"
	q += "slice of the string 'myString' that starts at the "+startPos[1]+"\n"
	q += "character and goes through (includes) the "+endPos[1]+"\n"
	q += "character.\n"

	resultVals = []
	for v in xVals:
		resultVals.append(eval("v["+startPos[0]+endPos[0]+"]"))

	a = 'result = myString['+startPos[0]+endPos[0]+']\n'
	
	me.setupCode = "    __ans=[]\n    for myString in "+str(xVals)+":\n"

	me.innerCheckCode = "        if 'result' in locals():__ans.append(result)\n"

	me.outerCheckCode = """\
if 'result' not in ld:
    print 'result not found.'
    sys.exit()
if __ans != """+str(resultVals)+""":
    print 'Incorrect answer(s).'
    print '''for data values: """+str(xVals)+""" the expected results are:'''
    print '''"""+str(resultVals)+""" but your results were:'''
    print str(__ans)
    sys.exit()
if len(ld) > 2:
    print 'Unneeded variable used.'
    sys.exit()"""
	
	return q,a    	
qq.genQFunc=qqq	
	


qq = Question(100)
qq.title = "String Repetition"
def qqq(n,me):
	if random.random() < .5:
		x = 'character'
	else:
		x = 'string'
	i = random.randint(20,50)
	l = random.randint(2,4)
	if x[0]=='c':l=1
	pos = random.randint(0,40)
	st = string.ascii_letters[pos:pos+l]
	q  = "Write a Python statement that replicates the\n"
	q += x+" '"+st+"' "+str(i)+" times.\n"
	q += "Name this string 'result'.\n"

	a = "result = '"+st+"'*"+str(i)+"\n\n  or\n\nresult = "+str(i)+"*'"+st+"'"
	resultVal = st*i
	
	# me.setupCode * not needed

	# me.innerCheckCode * not needed
	
	me.outerCheckCode = """\
if 'result' not in ld:
    print 'result not found.'
    sys.exit()
if result != '"""+resultVal+"""':
    print 'result should be:'
    print '"""+resultVal+"""'
    print 'but your result is:'
    print result 
    sys.exit()
if not '*' in __code_:
    print "Answer does not use the string repetition operator."
    sys.exit()
if len(ld) > 1:
    print 'Unneeded variable used.'
    sys.exit()"""
	
	return q,a    	
qq.genQFunc=qqq	
	


qq = Question(1)
qq.title = "Substring Existance"
def qqq(n,me):
	l = random.randint(1,4)
	pos = random.randint(0,40)
	st = string.ascii_letters[pos:pos+l]
	q  = "Write a Python statement to determine if the\n"
	q += "string referred to by variable 's1' is present\n"
	q += "in the string referred to by the variable 's2'.\n"
	q += "The variable 'result' should be True if it is\n"
	q += "and False if it is not."

	a = "result = s1 in s2"
	
	xVals = ['','12345',st,string.swapcase(st),st+'12345','12'+st+'34','1234'+st]
	
	resultVals = []
	for v in xVals:
		resultVals.append(st in v)

	me.setupCode  = "    s1='"+st+"'\n"
	me.setupCode += "    __ans=[]\n    for s2 in "+str(xVals)+":\n"

	me.innerCheckCode = "        if 'result' in locals():__ans.append(result)\n"

	me.outerCheckCode = """\
if 'result' not in ld:
    print 'result not found.'
    sys.exit()
if s1 != '"""+st+"""':
    print 'The value of s1 has been modified.'
    sys.exit()
if __ans != """+str(resultVals)+''':
    print 'Incorrect answer(s).  Searching for "'''+st+'''"'
    print "in: '''+str(xVals)+''' the expected results are:"
    print "'''+str(resultVals)+""" but your results were:"
    print str(__ans)
    sys.exit()
if len(ld) > 3:
    print 'Unneeded variable used.'
    sys.exit()"""
	
	return q,a    	
qq.genQFunc=qqq	
	


qq = Question(20)
qq.title = "Formatting Floating Point Numbers"
def qqq(n,me):
	num = random.random()*1000.
	dec = random.randint(1,5)
	wid = random.randint(11,20)
	q  = "Write a Python statement to format the floating\n"
	q += "point number referred to by variable 'f1'.\n"
	q += "It should have "+str(dec)+" decimal places and\n"
	q += "be in a field of total width "+str(wid)+".\n"
	q += "The variable 'result' should refer to the resulting\n"
	q += "string."

	a = 'result = "%'+str(wid)+'.'+str(dec)+'f" % (f1)'
	f1 = num
	xVal = num
	ans = '"%'+str(wid)+'.'+str(dec)+'f" % (f1)'
	resultVal = eval(ans)
	

	me.setupCode  = "        f1= "+str(num)+"\n"

	# me.innerCheckCode * not needed

	me.outerCheckCode = """\
if 'result' not in ld:
    print 'result not found.'
    sys.exit()
if f1 != """+str(num)+""":
    print 'The value of f1 has been modified.'
    sys.exit()
if not '%' in __code_:
    print 'Must use the string formatting operator.'
    sys.exit()
if result != '"""+str(resultVal)+"""':
    print 'Incorrect answer.   Expected result:'
    print "'"""+str(resultVal)+"""'",'but your answer was:'
    print "'"+result+"'"
    sys.exit()
if len(ld) > 2:
    print 'Unneeded variable used.'
    sys.exit()"""
	
	return q,a    	
qq.genQFunc=qqq	
	


qq = Question(20)
qq.title = "Formatting Strings"
def qqq(n,me):
	l = random.randint(4,10)
	pos = random.randint(0,40)
	s1 = string.ascii_letters[pos:pos+l]
	side = 'left'
	if random.random() <.5: side = 'right'
	sideChr = ''
	if side[0] == 'l': sideChr = '-'
	wid = random.randint(12,30)
	q  = "Write a Python statement to format the string\n"
	q += "referred to by variable 's1'.\n"
	q += "It should be "+side+" justified in a field of\n"
	q += "total width "+str(wid)+".  The variable \n"
	q += "'result' should refer to the resulting string.\n"

	a = 'result = "%'+sideChr+str(wid)+'s" % (s1)'
	xVal = s1
	ans = '"%'+sideChr+str(wid)+'s" % (s1)'
	resultVal = eval(ans)
	

	me.setupCode  = "        s1= '"+s1+"'\n"

	# me.innerCheckCode * not needed

	me.outerCheckCode = """\
if 'result' not in ld:
    print 'result not found.'
    sys.exit()
if s1 != '"""+s1+"""':
    print 'The value of s1 has been modified.'
    sys.exit()
if not '%' in __code_:
    print 'Must use the string formatting operator.'
    sys.exit()
if result != '"""+str(resultVal)+"""':
    print 'Incorrect answer.   Expected result:'
    print "'"""+str(resultVal)+"""'",'but your answer was:'
    print "'"+result+"'"
    sys.exit()
if len(ld) > 2:
    print 'Unneeded variable used.'
    sys.exit()"""
	
	return q,a    	
qq.genQFunc=qqq	
	


qq = Question(20)
qq.title = "Formatting Integers"
def qqq(n,me):
	num = random.randint(10,99999)
	side = 'left'
	if random.random() <.5: side = 'right'
	sideChr = ''
	if side[0] == 'l': sideChr = '-'
	wid = random.randint(8,20)
	q  = "Write a Python statement to format the integer\n"
	q += "referred to by variable 'num'.\n"
	q += "It should be "+side+" justified in a field of\n"
	q += "total width "+str(wid)+".  The variable \n"
	q += "'result' should refer to the resulting string.\n"

	a = 'result = "%'+sideChr+str(wid)+'d" % (num)'
	xVal = num
	ans = '"%'+sideChr+str(wid)+'d" % (num)'
	resultVal = eval(ans)
	

	me.setupCode  = "        num= "+str(num)+"\n"

	# me.innerCheckCode * not needed

	me.outerCheckCode = """\
if 'result' not in ld:
    print 'result not found.'
    sys.exit()
if num != """+str(num)+""":
    print 'The value of num has been modified.'
    sys.exit()
if not '%' in __code_:
    print 'Must use the string formatting operator.'
    sys.exit()
if result != '"""+str(resultVal)+"""':
    print 'Incorrect answer.   Expected result:'
    print "'"""+str(resultVal)+"""'",'but your answer was:'
    print "'"+str(result)+"'"
    sys.exit()
if len(ld) > 2:
    print 'Unneeded variable used.'
    sys.exit()"""
	
	return q,a    	
qq.genQFunc=qqq	
	


qq = Question(5)
qq.title = "Removing Characters from Strings"
def qqq(n,me):
	pool = string.ascii_letters+' \t   0123456789.",#$%^&*(){}[]=+'
	option = ['uppercase','lowercase','digits','whitespace','punctuation']
	myOpt = option[n]
	
	q  = "Write some Python code to remove all the\n"
	q += myOpt + " characters from the string 'myString'.\n"
	q += "myString should continue to refer to the original\n"
	q += "string and the variable 'result' should refer\n"
	q += "to the resulting string.\n"

	a = '''\
import string
result = ""
for ch in myString:
    if not ch in string.'''+myOpt+''':
        result += ch
'''

	xVals = []
	for i in range(5):
		siz = random.randint(15,25)
		st = ""
		for j in range(siz):
			st += random.choice(pool)
		xVals.append(st)
	
	exec("""\
resultVals = []
for myString in xVals:
    result = ""
    for ch in myString:
        if not ch in string."""+myOpt+""":
            result += ch
    resultVals.append(result)""")

	me.setupCode = "    __ans=[]\n    for myString in "+str(xVals)+":\n"

	me.innerCheckCode = "        if 'result' in locals():__ans.append(result)\n"

	me.outerCheckCode = """\
if 'result' not in ld:
    print 'result not found.'
    sys.exit()
if __ans != """+str(resultVals)+""":
    print 'Incorrect answer(s).'
    print '''for data values: """+str(repr(xVals))+""" the expected results are:'''
    print '''"""+str(repr(resultVals))+""" but your results were:'''
    print str(__ans)
    sys.exit()
if len(ld) > 4:
    print 'Unneeded variable used.'
    sys.exit()"""
	
	return q,a    	
qq.genQFunc=qqq	
	


qq = Question(1)
qq.title = "Find Index of First Occurence of Substring"
def qqq(n,me):
	f = random.randint(0,48)
	l = random.randint(1,3)
	s1 = string.ascii_letters[f:f+l]
	q  = "Write Python code to find the index of the first occurence\n"
	q += "of the string referred to by 's1' within the string\n"
	q += "'myString'.  Place this index in the variable 'result'.\n"
	q += "If 's1' does not appear in 'myString', set 'result' to -1.\n"
	q += "Do not change the value of either 's1' or 'myString'.\n"

	a = "result = myString.find(s1)"

	xVals = ['',s1,'1234567',s1+'123','12'+s1+'89','45678'+s1]
	
	exec("""\
resultVals = []
for myString in xVals:
    result = myString.find(s1)
    resultVals.append(result)""")

	me.setupCode  = "    s1 = '"+s1+"'\n"
	me.setupCode += "    __ans=[]\n    for myString in "+str(xVals)+":\n"

	me.innerCheckCode = "        if 'result' in locals():__ans.append(result)\n"

	me.outerCheckCode = """\
if 'result' not in ld:
    print 'result not found.'
    sys.exit()
if s1 != '"""+s1+"""':
    print 's1 has been modified.'
    sys.exit()
if __ans != """+str(resultVals)+""":
    print 'Incorrect answer(s).  Searching for "'+s1+'" in these strings:'
    print '''"""+str(repr(xVals))+""".  The expected results are:'''
    print '"""+str(repr(resultVals))+""" but your results were:'
    print str(__ans)
    sys.exit()
if len(ld) > 3:
    print 'Unneeded variable used.'
    sys.exit()"""
	
	return q,a    	
qq.genQFunc=qqq	
	


qq = Question(100)
qq.title = "String Methods"
def qqq(n,me):
	ops = ['upper','lower','swapcase','title','capitalize','center']
	text= ['changing all the cased characters to upper case',
		   'changing all the cased characters to lower case',
		   'changing the case of each cased character',
		   'setting the case of the first letter of each word to upper\n'+\
		   'and the case of other letters to lower',
		   'setting the case of the first character to upper\n'\
		   'and all others to lower',
		   'centering the string in a field of the specified width']
		   
	op = random.randint(0,5)
	wid = random.randint(45,70)

	q  = "Write Python code to modify the string referred to by\n"
	q += "'myString'.  Do this by\n"
	q += text[op]+"\n"
	q += "and setting the variable 'result' to your changed string.\n"
	if op == 5: q+= "\nUse a field width of "+str(wid)+".\n"

	a = "result = myString."+ops[op]+"()"
	if op == 5: a = "result = myString."+ops[op]+"("+str(wid)+")"
	
	st = list(titles)
	random.shuffle(st)
	xVals = []
	for i in range(3):
		xVals.append(st[i])

	exec("""\
resultVals = []
for myString in xVals:
    """+a+"""
    resultVals.append(result)""")

	me.setupCode = "    __ans=[]\n    for myString in "+str(xVals)+":\n"

	me.innerCheckCode = "        if 'result' in locals():__ans.append(result)\n"

	me.outerCheckCode = """\
if 'result' not in ld:
    print 'result not found.'
    sys.exit()
if __ans != """+str(resultVals)+""":
    print 'Incorrect answer(s).  Given these strings:'
    print '''"""+str(repr(xVals))+""".  The expected results are:'''
    print '''"""+str(repr(resultVals))+""" but your results were:'''
    print str(__ans)
    sys.exit()
if len(ld) > 2:
    print 'Unneeded variable used.'
    sys.exit()"""
	
	return q,a    	
qq.genQFunc=qqq	
	


