#!/usr/bin/python
title = u'Question Generator  version 2.00        The subject content is copyright \u00a9 2011 by Leon Tietz'

import Tkinter
import Pmw
import qGen2Support
import glob
import os
import subprocess
import time
import signal
from dialogStuff import *

startStr = "# You must select a question before entering any code.\n# Press 'Cancel'."

def doUserCode(par, prompt, x=None, y=None):
    global startStr
    gframe = EditStringDialog(par, prompt, startStr, x, y)
    while True:
        val = gframe.show()
        if val is None:  # User pressed 'Cancel' button
            gframe.destroy()
            return
        # 'Submit' button was pressed.
        val = val.strip()
        startStr = val
        if curQues.loopingCode: val = loopingFixup(val)
        graderResult = grader(val)
        if not graderResult:  # Answer is OK (None was returned)
            viewAnalysis(gframe,"         Correct!         ","dark green")
            break
        else:  # A user-code error was detected.  Show diagnosis.
            viewAnalysis(gframe,graderResult,"dark red")
    gframe.destroy()  # Remove the code-entry window
    return

# This will be used to permit looping user code with differing test data 
def loopingFixup(val):
    return val

def grader(userCode):
    # Wrap testing code around the userCode and analyze the result
    # Return None if answer is correct, else return a string describing the error
    outFile = open("_tester.py", 'w')  # create the file that will be used to execute the user code.

    # Create preamble code used for all quesions.  Copy namespace to analyze variable usage later
    outFile.write("import inspect as __inspect\n\n")
    outFile.write("# Code to set up environment for testing student code\n\n")
    outFile.write("# make a copy of the local namespace and remove all entries beginning with '__'\n")
    outFile.write("_ld = locals().copy()\n")
    outFile.write("for __key in _ld.keys():\n")
    outFile.write("	if __key[:2] == '__': del(_ld[__key])\n")

    # User code will be in a try/except block
    outFile.write("try:\n")
    
    # Include the question-dependent code that must run before the user code
    outFile.write("\n"+curQues.setupCode+"\n")

    # Save copy of user code for regular expression analysis
    outFile.write("        __code_ = '''\n"+userCode+"\n'''\n")
    
    # Grab current line number to have more meaningful error messages, if necessary
    outFile.write("        _lno = __inspect.currentframe().f_lineno\n")

    # User code is wrapped in statement statement type (eval or exec) as specified in Question object
    outFile.write('        '+curQues.wrapper+'("""\\\n')
    
    outFile.write(userCode)

    outFile.write('\n""")\n')

    # Include question-dependent code to analyze result while inside try/except.  
    outFile.write("\n"+curQues.innerCheckCode+"\n")
    
    # Except block will catch syntax and run-time errors
    outFile.write("except Exception, x:\n")
    outFile.write("    import sys\n")
    outFile.write("    import traceback\n")
    outFile.write("    et, ev, tb = sys.exc_info()\n")                                                 
    outFile.write("    lno = traceback.tb_lineno(tb)\n")    
    outFile.write("    print 'Error:',x\n")
    outFile.write("    if not 'line' in str(x):\n")
    outFile.write("        print 'on or near line', lno-_lno-2, 'of submitted code.'\n")
    outFile.write("    sys.exit()\n\n")   # Leave if error detected

    # Copy namespace after user code execution
    outFile.write("# make a copy of the local namespace and remove all entries beginning with '_'\n")
    outFile.write("ld = locals().copy()\n")
    outFile.write("for key in ld.keys():\n")
    outFile.write("    if key[0] == '_': del(ld[key])\n")
    outFile.write("import sys\n")

    # Include question-dependent code to analyze result of user code execution.  This code will cause an
    # exit if an error is found.
    outFile.write("\n"+curQues.outerCheckCode+"\n")

    # Add code to test file to write an unique, easily to test for key (no errors were detected)
    key = "key = " + str(random.randint(10000,99999))
    outFile.write("\nprint '"+key+"'\n")
    outFile.close()

    # This block of code runs the user code and the wrapper code used for its analysis created above
    # and allows the program to recover if user code is an infinite loop.
    p=subprocess.Popen('python _tester.py >_testerOut.txt 2>&1', shell = True) # Run code as new subprocess
    cnt = 0
    while type(p.poll()) == type(None):
    	cnt += 1
    	if cnt >6:
    	    if os.name == 'posix':  # kill task in Mac or Linux O/S
                os.kill(p.pid,signal.SIGKILL)
            else:  # kill task in Windows O/S
                os.system("taskkill /pid %i /f >>junk.txt"%(p.pid))
        time.sleep(0.2)
    if p.returncode:  # O/S provided a non-zero return code (was killed)
        all = "Did not finish.  Task killed!"

    # Get results of execution of user code
    else:
        inFile = open("_testerOut.txt",'rU')
        all = inFile.read()
        inFile.close()

    # key will have been printed only if all specified tests pass
    if key in all:
        return None
    return all

# A pop-up window with analysis of execution of user code
def viewAnalysis(root,textToShow,textColor): 
    showAnal = Pmw.Dialog(root, buttons=('OK',), title='Answer Analysis')
    w = Tkinter.Label(showAnal.interior(), text=textToShow, pady=20,\
            justify=Tkinter.LEFT,fg=textColor,font = ("Courier", 12, "bold"))
    w.pack(expand=1, fill=Tkinter.BOTH, padx=4, pady=4)
    showAnal.activate()  # Display the window
    showAnal.destroy()   # Remove the window


qSeed = qGen2Support.rand4()
qN = -1
qNmin = 0
qNmax = 99

# Helper functions for range and validation in the Question # Selection Widget
def _counter(text, factor, increment):
	textInt = int(text)
	if factor == 1:
		textInt += 1
		return str(min(textInt,qNmax))
	else:
		textInt -= 1
		return str(max(textInt,0))  		
def _validate(text):
	try:
		val = int(text)
	except:
		return -1
	if val < qNmin: return -1
	if val > qNmax:	return -1
	return 1

qAns = "Select a question before requesting an anwser."
curQues = None

class qGen:
    def __init__(self, parent):
        # Create the ScrolledCanvas.
        self.sc = Pmw.ScrolledCanvas(parent,
			borderframe = 1,
			labelpos = 'n',
			label_text = 'Question Display Window',
			usehullsize = 1,
			hull_width = 500,
			hull_height = 250,
		)
        # A list to keep track of the objects placed on the canvas so they
        # can easily be deleted.
        self.scObjs = []
        self.qSet = ""
        
        # Create a group for the Exit Buttons
        xx = Pmw.Group(parent)
        xx.pack(side = 'bottom')
        
        # Create Button to display exit qGen
        buttonBox = Pmw.ButtonBox(xx.interior())
        buttonBox.pack(side = 'left',padx = 50)
        buttonBox.add('exit', text = 'Exit', command = root.destroy)

        # Create Button to display do email report and exit qGen
        buttonBox = Pmw.ButtonBox(xx.interior())
        buttonBox.pack(side = 'right',padx = 50)
        buttonBox.add('report', text = 'Send Progress Report & Exit', command = root.destroy)
        
        # Create a group widget to contain the scrollmode options.
        w = Pmw.Group(parent, tag_text='Chapter ' + str(chapter) + ' Question Selector')
        w.pack(side = 'bottom', padx = 5, pady = 5)

        # Create Random Seed Widget
        self.Seed = Pmw.Counter(w.interior(),
            labelpos = 'n',
            label_text = 'Random Seed',
            orient = 'horizontal',
            entry_width = 5,
            entryfield_value = qSeed,
            entryfield_validate = {'validator' : 'integer',
                'min' : 0, 'max' : 9999}
        )
        self.Seed.pack(side = 'left', padx = 10, pady = 5)

        # Create Question Type Selector Widget
        qt = Pmw.OptionMenu(w.interior(),
            labelpos = 'n',
            label_text = 'Question Type:',
            items = qdocs, 
            command = self.getQTypeData,
            menubutton_width = 50,
        )
        qt.pack(side = 'left', padx = 5, pady = 5)
        qt.invoke(0)

        # Create Question Number Selection Widget
        self.QNum = Pmw.Counter(w.interior(),
            labelpos = 'n',
            label_text = 'Question #',
            orient = 'horizontal',
            entry_width = 2,
            entryfield_value = 0,
            datatype = {'counter' : _counter},
            entryfield_validate = _validate
        )
        self.QNum.pack(side = 'left', padx = 10, pady = 5)

        # Pack Widgets
        x = Pmw.Group(parent,tag_text='Select an Action')
        x.pack(side = 'bottom', padx = 5, pady = 5)

        # Create Button to allow Code Entry
        buttonBox = Pmw.ButtonBox(x.interior())
        buttonBox.pack(side = 'left',padx = 10)
        buttonBox.add('code', text = 'Write Python Code for this Question', command = lambda win=root,\
                      prompt="Python Code Entry Window": doUserCode(win,prompt))

        # Create Button to display answer to current question
        buttonBox = Pmw.ButtonBox(x.interior())
        buttonBox.pack(side = 'left',padx = 10)
        buttonBox.add('view', text = 'View Answer', command = self.viewAns)

        # Create Button to display next question
        buttonBox = Pmw.ButtonBox(x.interior())
        buttonBox.pack(side = 'left',padx = 10)
        buttonBox.add('nextQ', text = 'Display (Next) Question', command = self.showNQuest)
        
        # Pack buttons
        self.sc.pack(padx = 5, pady = 5, fill = 'both', expand = 1)

        
        
        # Create initial display
        self.scObjs.append(self.sc.create_text(20, 20, anchor = 'nw',
            text = 'To begin using this Question Generator you need only:\n\n'
                   '1) Select the Question Type.\n'
                   '2) Press "Display (Next) Question"\n'
                   '3) Click "Write Code for Question" or "View Answer"\n'
                   '4) When complete, repeat step 1 or 2 or click "Exit".\n\n'
                   'Other features:\n\n'
                   '-Each question has a four-part code number of the form: chapter-seed-quesType-quesNum\n'
                   '-Please use this code number to identify a question when providing feedback and reporting bugs.\n'
                   '-The Random Seed and Question # can be set to return to any question you have seen in the past\n'
                   ' assuming you remember these numbers.'                  
                   ,
            font = ("Times", 10, "bold")))
     
        # Set the scroll region of the canvas to include all the items just created.
        self.sc.resizescrollregion()
    
	# Called from Question Type Selector Widget
    def getQTypeData(self, tag):
        global qNmax,qN
        self.qType = tag
        qInd = int(tag[0:int(string.find(self.qType,')'))])
        qNmax = Question.qList[qInd].count - 1
        qN = min(qNmax, qN)
        random.seed(int(self.Seed.getvalue())*100 + qN)
        qt = int(self.qType[0:string.find(self.qType,')')])
        qNmax = Question.qList[qt].count-1
        

    # Run this when the Display (Next) Question button is pressed
    # Result depends on whether question selector has been modified
    def showNQuest(self):
        global qN
        x = int(self.QNum.getvalue())
        if x == qN:  # needed if user has switched to a ques type with fewer questions
            if qN >= qNmax:
                qN = qNmin
            else:    # increment ques number
                qN += 1
        else:
            qN = min(x, qNmax)
        self.QNum.setvalue(qN)
        self.showQuest()
        
    # Run this when the View Answer button is pressed    
    def viewAns(self): 
        showAns = Pmw.Dialog(root, buttons=('OK',), title='Answer')
        w = Tkinter.Label(showAns.interior(), text=qAns, pady=20, justify=Tkinter.LEFT,fg="blue",\
                          font = ("Courier", 12, "bold"))
        w.pack(expand=1, fill=Tkinter.BOTH, padx=4, pady=4)
        showAns.activate()
        showAns.destroy()
        
    # Control the display of a question    
    def showQuest(self):
        global qN, qSeed, qAns, startStr, curQues
        # when using a canvas, it works best to keep a list of the objects displayed.  They can
        # then be easily deleted before a new display is created.
        for obj in self.scObjs:
            self.sc.delete(obj)
        self.scObjs = []
        self.img = []
        startStr = "# Click to enter your code here."
        qSeed = int(self.Seed.getvalue())  # get displayed random seed
        
        qt = int(self.qType[0:string.find(self.qType,')')])
        qNmax = Question.qList[qt].count-1
        # Generate a randomized list for question selection from a data set
        random.seed(qSeed)
        self.qNr = range(qNmax+1)
        random.shuffle(self.qNr)
        
        rQnum = self.qNr[qN]  # question selection is from randomized list
        curQues = Question.qList[qt]  # curQues is Question object of selected type
        random.seed(qSeed*100 + qN)       # Seed rng based on displayed seed and ques num
                                          # The result is randomized, but reproducible
        q,a = curQues.genQ(rQnum,curQues)     # get ques and ans for this q#
        n = "Q=%d-%d-%d-%d"%(chapter,qSeed,qt,qN)  # code number to uniquely identify question
        self.scObjs.append(self.sc.create_text(30,20, anchor = 'nw', text=n,
                            font = ("Times", 12, "bold")))
        self.render([('text',(30,60),'navy',q)])  # display question
        qAns = "The answer can be written as:\n\n"+a  # Prep answer for display
        self.sc.resizescrollregion()
        self.sc.yview_moveto(0)

    # place various objects in the question display window.  'text' is the usual one.  Others are
    # left-over from original qGen.
    def render(self,tups):
        for (t,xy,opt,dat) in tups:
            if t=='text':
                self.scObjs.append(self.sc.create_text(xy[0],xy[1],anchor='nw',fill=opt,text=dat,
                                font = ("Courier", 10, "bold")))
            elif t=='bitmap':
                self.img.append(Tkinter.BitmapImage(file='images\\'+dat))
                self.scObjs.append(self.sc.create_image(xy[0], xy[1], image=self.img[-1], anchor=Tkinter.CENTER))
            elif t=='line':
                self.scObjs.append(self.sc.create_line(xy[0],xy[1],xy[2],xy[3],width=dat,fill=opt)) 
            elif t=='dot':
       	        self.scObjs.append(self.sc.create_oval(xy[0]-dat,xy[1]-dat,xy[0]+dat,xy[1]+dat,fill=opt))                
            elif t=='rect':
                self.scObjs.append(self.sc.create_rectangle(xy[0],xy[1],xy[2],xy[3],width=dat,outline=opt)) 

######################################################################

class GetQuestionSet:
    def __init__(self, parent):

        # Create the ScrolledListBox.
        self.box = Pmw.ScrolledListBox(parent,
            items=quesSets,
            labelpos='nw',
            label_text='Question Sets',
            listbox_height = 6,
            selectioncommand=self.selectionCommand,
            dblclickcommand=root.destroy,
            usehullsize = 1,
            hull_width = 400,
            hull_height = 200,
        )
        self.box.pack()
        
    def selectionCommand(self):
        global quesSet
        sels = self.box.getcurselection()
        quesSet = sels[0]

# Find available question sets
quesSets = glob.glob("*.ques")
# Remove .ques from question set name
for i in range(len(quesSets)):
    quesSets[i] = quesSets[i][:-5]
# Append an option for quitting
quesSets.append("*** Quit ***")

# Get the desired question set from user
if __name__ == '__main__':
    while True:
        # Create and execute initial window to get chapter/question set from user
        quesSet = ""
        root = Tkinter.Tk()
        Pmw.initialise(root)
        root.title("Select a Question Set and Click OK")
        exitButton = Tkinter.Button(root, text = 'OK', command = root.destroy)
        exitButton.pack(side = 'bottom')
        GetQuestionSet(root)   # see class just above
        root.mainloop()   # Get chapter data from user
    
        if len(quesSet) == 0 or quesSet == "*** Quit ***": break # No selection or Quit selected
        execfile(os.path.join(quesSet+'.ques','ques.py'))  # Read/Compile the file of questions

        # Create question selection list for selected chapter/question set
        qdocs = []
        for q in range(len(Question.qList)):
            qdocs.append(str(q)+") "+Question.qList[q].title+"   "+ str(Question.qList[q].count)+" question(s)")
        qdocs = tuple(qdocs)
        qNmax = Question.qList[0].count - 1

        # Create an instance of qGen
        root = Tkinter.Tk()
        Pmw.initialise(root)
        root.title(title)
#        exitButton = Tkinter.Button(root, text = 'Exit', command = root.destroy)
#        exitButton.pack(side = 'bottom')
        qGen(root)
        root.mainloop()      # run qGen
        Question.qList = []  # Empty the qList to prevent appending to existing with next selection
