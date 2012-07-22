
# This is the class that is used to define questions.  This class is subject to have additions as new question types are added.
class Question(object):
    qList = []
	
    def __init__(self,count):
        Question.qList.append(self)
        self.title = "Title not yet defined."
        self.count = count
        self.q     = "Question not yet defined."
        self.genQFunc = None
        self.setupCode = "# Unitialized setupCode."
        self.innerCheckCode = "# Unitialized innerCheckCode."
        self.outerCheckCode = "# Unitialized outerCheckCode."
        self.wrapper = "exec"
        self.loopingCode = ""
        
    def genQ(self,rQnum,me):
    	return self.genQFunc(rQnum,me)
		
    def genAnsStr(self):
        return "Answer string not defined."

    def __str__(self):
        return "Question: " + self.title + " (" + str(self.count) + " variations)"
		

if __name__ == '__main__':
    a = Question(2)
    b = Question(5)
    c = Question(100)
    print len(Question.qList)
    for q in Question.qList:
        print q
        print q.testCheck()

    raw_input("Press a key.")
	
