import random
import string
import qGen2Support
from quesSupport import *
from dataSets import *

chapter = 1


qq = Question(len(unitConv)*2)	# Create Q type (twice as many questions as data set elements)
qq.title = "Unit Conversion"
def qqq(n,me):
	l = len(unitConv)	# get length of this data set
	u1 = unitConv[n % l][0]
	u2 = unitConv[n % l][1]
	ux = float(unitConv[n % l][2])
	if n >= l:
		u1,u2 = u2,u1
		ux = 1/ux
		
	q = "Write a Python statement to calculate "+u2+" given "+u1+".\n"+\
	    "Use '"+u2+"' and '"+u1+"' as your variable names.\n"+\
		"If you don't know the conversion factor, you will need to look it up."
	
	val1 = qGen2Support.fpTruncate(ux,6)
	val2 = qGen2Support.fpTruncate(1./ux,6)
	a = "%s = %s * %s\n  or\n%s = %s / %s" % (u2,u1,val1,u2,u1,val2)
	
	givenVal = (random.random()+.05)*99
	ansVal1 = givenVal * ux * 0.9999
	ansVal2 = givenVal * ux * 1.0001
	
	me.setupCode = "    for "+u1+" in [" + str(givenVal) + "]:\n"
	
	# me.innerCheckCode * not needed
	
	me.outerCheckCode = "if '"+u2+"' not in ld:\n    print '"+u2+" not found.'\n    sys.exit()\n"+\
	                  "if '"+u1+"' not in ld:\n    print '"+u1+" missing.'\n    sys.exit()\n"+\
			  "if not("+str(ansVal1)+"<"+u2+"<"+str(ansVal2)+"):\n"\
			      "    print 'Computation is wrong'\n    sys.exit()\n"+\
			  "if len(ld) > 2:\n    print 'Unneeded variable used.'\n    sys.exit()\n"
	return q,a    	
qq.genQFunc=qqq


qq = Question(len(pairs))
qq.title = "Generic Variable Swap"
def qqq(n,me):
	l = len(pairs)	# get length of this data set
	v1 = pairs[n % l][0]
	v2 = pairs[n % l][1]
		
	q = "Write Python statements to swap (exchange the values of) "+v1+" and "+v2+".\n"+\
	    "Use one additional variable to do this."
	
	a = "%s = %s\n%s = %s\n%s = %s" % ('temp',v1,v1,v2,v2,'temp')
	
	val1 = random.randint(100,999)
	val2 = val1 + random.randint(20,100)
	me.setupCode = "    for "+v1+","+v2+" in [("+str(val1)+','+str(val2)+")]:\n"

	# me.innerCheckCode * not needed
		
	me.outerCheckCode = "if '"+v2+"' not in ld:\n    print '"+v2+" not found.'\n    sys.exit()\n"+\
	                  "if '"+v1+"' not in ld:\n    print '"+v1+" missing.'\n    sys.exit()\n"+\
			  "if "+v1+" != "+str(val2)+" or "+v2+" != " +str(val1)+":\n"\
			      "    print 'Computation is wrong'\n    sys.exit()\n"+\
			  "if len(ld) > 3:\n    print 'Unneeded variable used.'\n    sys.exit()\n"+\
			  "if len(ld) < 3:\n    print 'Additional variable not used.'\n    sys.exit()\n"
	return q,a    	
qq.genQFunc=qqq


qq = Question(len(pairs))
qq.title = "Python-style Variable Swap"
def qqq(n,me):
	l = len(pairs)	# get length of this data set
	v1 = pairs[n % l][0]
	v2 = pairs[n % l][1]
		
	q = "Write Python statements to swap (exchange the values of) "+v1+" and "+v2+".\n"+\
	    "Do this with a single Python statement."
	
	a = "%s,%s = %s,%s" % (v1,v2,v2,v1)
	
	val1 = random.randint(100,999)
	val2 = val1 + random.randint(20,100)
	
	me.setupCode = "    for "+v1+","+v2+" in [("+str(val1)+','+str(val2)+")]:\n"

	# me.innerCheckCode * not needed
	
	me.outerCheckCode = "if '"+v2+"' not in ld:\n    print '"+v2+" not found.'\n    sys.exit()\n"+\
	                  "if '"+v1+"' not in ld:\n    print '"+v1+" missing.'\n    sys.exit()\n"+\
			  "if "+v1+" != "+str(val2)+" or "+v2+" != " +str(val1)+":\n"\
			      "    print 'Computation is wrong'\n    sys.exit()\n"+\
			  "if len(ld) > 2:\n    print 'Unneeded variable used.'\n    sys.exit()"
	return q,a    	
qq.genQFunc=qqq


qq = Question(len(vars))
qq.title = "Initialize an Integer to a Constant"
def qqq(n,me):
	var = vars[n]
	val = random.randint(5,90)

	q = "Write a Python statement to set the variable '"+var+"' to the integer value "+str(val)+"."

	a = "%s = %d"%(var,val)

	# me.setupCode  * not needed

	# me.innerCheckCode * not needed
	
	me.outerCheckCode = "if '"+var+"' not in ld:\n    print '"+var+" not found.'\n    sys.exit()\n"+\
			   "if type("+var+") != type(1):\n    print 'Assigned value has wrong type.'\n    sys.exit()\n"+\
			   "if "+var+" != "+str(val)+":\n    print 'Assigned value is wrong'\n    sys.exit()\n"+\
			   "if len(ld) > 1:\n    print 'Unneeded variable used.'\n    sys.exit()"
	return q,a    	
qq.genQFunc=qqq	
	

qq = Question(len(vars))
qq.title = "Initialize a Float to a Constant"
def qqq(n,me):
	var = vars[n]
	valStr = str(random.randint(1,99)) + '.' + str(random.randint(1,99))
	val = float(valStr)

	q = "Write a Python statement to set the variable '"+var+"' to the float value "+valStr+"."

	a = "%s = %s"%(var,valStr)

	# me.setupCode  * not needed

	# me.innerCheckCode * not needed
	
	me.outerCheckCode = "if '"+var+"' not in ld:\n    print '"+var+" not found.'\n    sys.exit()\n"+\
			   "if type("+var+") != type(1.0):\n    print 'Assigned value has wrong type.'\n    sys.exit()\n"+\
			   "if "+var+" != "+valStr+":\n    print 'Assigned value is wrong'\n    sys.exit()\n"+\
			   "if len(ld) > 1:\n    print 'Unneeded variable used.'\n    sys.exit()"
	return q,a    	
qq.genQFunc=qqq	
	

qq = Question(len(vars))
qq.title = "Initialize a Long Integer to a Constant"
def qqq(n,me):
	var = vars[n]
	val = random.randint(5,990)

	q = "Write a Python statement to set the variable '"+var+"' to the long integer value "+str(val)+"."

	a = "%s = %dL"%(var,val)

	# me.setupCode  * not needed

	# me.innerCheckCode * not needed
	
	me.outerCheckCode = "if '"+var+"' not in ld:\n    print '"+var+" not found.'\n    sys.exit()\n"+\
			   "if type("+var+") != type(1L):\n    print 'Assigned value has wrong type.'\n    sys.exit()\n"+\
			   "if "+var+" != "+str(val)+"L:\n    print 'Assigned value is wrong'\n    sys.exit()\n"+\
			   "if len(ld) > 1:\n    print 'Unneeded variable used.'\n    sys.exit()"
	return q,a    	
qq.genQFunc=qqq	
	

qq = Question(len(vars))
qq.title = "Initialize a Boolean Variable"
def qqq(n,me):
	var = vars[n]
	val = True
	if random.random() < .5:
		val = False
	valStr = str(val)
	
	q = "Write a Python statement to set the variable '"+var+"' to "+valStr+"."

	a = "%s = %s"%(var,valStr)

	# me.setupCode  * not needed

	# me.innerCheckCode * not needed
	
	me.outerCheckCode = "if '"+var+"' not in ld:\n    print '"+var+" not found.'\n    sys.exit()\n"+\
			   "if type("+var+") != type(True):\n    print 'Assigned value has wrong type.'\n    sys.exit()\n"+\
			   "if "+var+" != "+valStr+":\n    print 'Assigned value is wrong'\n    sys.exit()\n"+\
			   "if len(ld) > 1:\n    print 'Unneeded variable used.'\n    sys.exit()"
	return q,a    	
qq.genQFunc=qqq	
	

qq = Question(100)
qq.title = "Initialize a String Variable"
def qqq(n,me):
	l = len(stngs) # get length of this data set
	line = random.randrange(0,l)
	var = stngs[line][0]
	val = stngs[line][random.randrange(1,len(stngs[line]))]
	
	q = "Write a Python statement to set the variable '"+var+"' to "+'"'+val+'".'

	a = '%s = "%s"'%(var,val)

	# me.setupCode  * not needed

	# me.innerCheckCode * not needed
	
	me.outerCheckCode = "if '"+var+"' not in ld:\n    print '"+var+" not found.'\n    sys.exit()\n"+\
			   "if type("+var+") != type(' '):\n    print 'Assigned value has wrong type.'\n    sys.exit()\n"+\
			   "if "+var+" != '"+val+"':\n    print 'Assigned value is wrong'\n    sys.exit()\n"+\
			   "if len(ld) > 1:\n    print 'Unneeded variable used.'\n    sys.exit()"
	return q,a    	
qq.genQFunc=qqq	
	

qq = Question(100)
qq.title = "Write an Integer Arithmetic Expression"
qq.wrapper = "x = eval"
def qqq(n,me):
	n1 = random.randrange(2,20)
	n2 = random.randrange(2,20)
	n3 = random.randrange(1,2000)

	op = "add"
	opSym = "+"
	n4 = n3
	if random.random() < 0.5:
		op = "subtract"
		opSym = "-"
		n4 = -n4
	
	ans = n1*n2+n4
	
	q = "Write a Python expression to compute the following:\n\n"+\
	    "Multiply n1 by n2.  Then "+op+" the integer " +str(n3)+"."

	a = 'n1 * n2 %s %d'%(opSym,n3)

	me.setupCode = "    for n1,n2 in [("+str(n1)+','+str(n2)+")]:\n"

	# me.innerCheckCode * not needed
	
	me.outerCheckCode = "if type(x) != type(1):\n    print 'Produced value has wrong type.'\n    sys.exit()\n"+\
			    "if x != "+str(ans)+":\n    print 'Calculated value is wrong'\n    sys.exit()\n"+\
			    "if len(ld) > 3:\n    print 'Unneeded variable used.'\n    sys.exit()"
	return q,a    	
qq.genQFunc=qqq	
	

qq = Question(len(modules))
qq.title = "Using Import Statements"
def qqq(n,me):
	mod = modules[n][0]
	desc = modules[n][1]
		
	q = "The "+mod+ " module "+desc+".\n\n"+\
	    "Write a Python statements to make this functionality available to a program."
	
	a = "import " + mod
	
	# me.setupCode  * not needed

	# me.innerCheckCode * not needed
	
	me.outerCheckCode = "if '"+mod+"' not in ld:\n    print 'Requested module not imported.'\n    sys.exit()\n"+\
			  "if type("+mod+") != type(sys):\n    print 'Module was not imported.'\n    sys.exit()\n"+\
			  "if len(ld) > 1:\n    print 'Unneeded variable used.'\n    sys.exit()\n"
	return q,a    	
qq.genQFunc=qqq


qq = Question(100)
qq.title = "Modify an Integer Variable's Value"
def qqq(n,me):
	op = random.randrange(0,5)
	n1 = random.randrange(2000,20000)
	n2 = random.randrange(2,200)

	q = "Write a Python statement that modifies the integer variable 'x' by\n"

	if op == 0: # addition
		q += "adding "+str(n2)+" to it."
		ans = n1+n2
		a = "x = x + "+str(n2)+"\n  or\nx += "+str(n2)
	if op == 1: # subtraction
		q += "subtracting "+str(n2)+" from it."
		ans = n1-n2
		a = "x = x - "+str(n2)+"\n  or\nx -= "+str(n2)
	if op == 2: # multiplication
		q += "multiplying it by "+str(n2)+"."
		ans = n1*n2
		a = "x = x * "+str(n2)+"\n  or\nx *= "+str(n2)
	if op == 3: # division
		q += "dividing it by "+str(n2)+"."
		ans = n1/n2
		a = "x = x / "+str(n2)+"\n  or\nx /= "+str(n2)
	if op == 4: # modulus
		q += "assigning it the remainder when dividing it by "+str(n2)+"."
		ans = n1%n2
		a = "x = x % "+str(n2)+"\n  or\nx %= "+str(n2)

	me.setupCode = "    for x in [" + str(n1) + "]:\n"

	# me.innerCheckCode * not needed
	
	me.outerCheckCode = "if 'x' not in ld:\n    print 'x not found.'\n    sys.exit()\n"+\
			   "if type(x) != type(1):\n    print 'Assigned value has wrong type.'\n    sys.exit()\n"+\
			   "if x != "+str(ans)+":\n    print 'Assigned value is wrong'\n    sys.exit()\n"+\
			   "if len(ld) > 1:\n    print 'Unneeded variable used.'\n    sys.exit()"
	
	return q,a    	
qq.genQFunc=qqq	
	

qq = Question(100)
qq.title = "Compute Shopping Cart Value"
def qqq(n,me):
	l = len(cart)
	selector = range(l)
	random.shuffle(selector)
	count = random.randint(3,5)
	selector = selector[:count]

	q = "Write a Python statement that computes 'total', the value of the\nitems in this shopping cart.\n\n"
	q += "Quantity  Description        Unit Cost"

	a = "total = "
	total = 0
	for i in selector:
		cnt = random.randint(1,cart[i][2])
		q += "\n%8d  %-17s %10s"%(cnt,cart[i][0],cart[i][1])
		total += cnt*(float(cart[i][1][1:]))
		if cnt>1:
			a += str(cnt)+"*"
		a += cart[i][1][1:]+" + "
	a = a[:-3]
	totalStr = "%10.2f"%(total)
	
	# me.setupCode  * not needed

	# me.innerCheckCode * not needed
	
	me.outerCheckCode = "if 'total' not in ld:\n    print 'total not found.'\n    sys.exit()\n"+\
			   "if type(total) != type(1.0):\n    print 'Assigned value has wrong type.'\n    sys.exit()\n"+\
			   "totStr = '%10.2f'%(total)\n"+\
			   "if totStr != '"+totalStr+"':\n    print 'Assigned value is wrong'\n    sys.exit()\n"+\
			   "if len(ld) > 1:\n    print 'Unneeded variable used.'\n    sys.exit()"
	
	return q,a    	
qq.genQFunc=qqq	
	
