# Note: ModalDialog and EditStringDialog were found on the web and only modified slightly.
# I found these uncommented and need to spend some time commenting them (soon???)

import Tkinter

class ModalDialog(Tkinter.Toplevel):

    def __init__(self, parent, x, y, title):
        Tkinter.Toplevel.__init__(self, parent)
        self.transient(parent)
        self.title(title)
        self.protocol( 'WM_DELETE_WINDOW', self.cancel)
        self.value=None
        self.x = x
        self.y = y

        # NEED TO HIDE UNTIL SHOWN
        # NEED TO POSITION REGARD TO X, Y

    def show( self ):
        self.position()
        oldFoc = self.focus_get()
        self.focus_set()
        self.grab_set()
        self.lift()
        self.deiconify()
        self.update()
        self.mainloop()
        self.grab_release()
        if oldFoc:
           oldFoc.focus_set()
        return self.value

    def returnValue(self):
        self.quit()

    def cancel(self):
        self.value=None
        self.quit()

    def position(self):
        # We want the window displayed hidden in case it is moved
        self.withdraw()
        self.update()

        # Position the window at x,y
        # Ensure the window will not go off screen
        # windims are like '30x40+50+50'
        # 30x40 is the size, the rest is startpos

        maxX, maxY = self.maxsize()
        maxY -= 40
        windims = self.geometry().split('+')[0].split('x')
        width=int(windims[0])
        height=int(windims[1])

        if self.x == None or self.y == None:
            self.x=(maxX-width)/2
            self.y=(maxY-height)/2

        if (self.x+width) > maxX: self.x = maxX - width
        if (self.y+height) > maxY: self.y = maxY - height

        # Now position the window and show it.
        self.geometry("+"+str(self.x)+"+"+str(self.y))
        self.update()

class EditStringDialog(ModalDialog):

    def __init__(self, parent, prompt, startValue, x, y):
        ModalDialog.__init__(self, parent, x, y, prompt)
        self.config(bg="white")
        self.value=startValue

        self.ew=Tkinter.Text(self, bg="white",  width=60, borderwidth=0, height=10, font=('Courier','14'))

        if startValue:
            self.ew.insert("1.0", startValue)
        self.ew.pack(side="top", fill="both", padx=5, expand=True)

        bframe=Tkinter.Frame(self, bd=10)
        bframe.pack(side="top", fill="x")

        okBut=Tkinter.Button(bframe, text="Submit", command=self.returnValue, underline=False, default="active")
        cancelBut = Tkinter.Button(bframe, text="Cancel", command=self.cancel, underline=False)

        okBut.pack(side="left")
        cancelBut.pack(side="right")

    def returnValue(self):
        self.value=self.ew.get("1.0", Tkinter.END)
        self.quit()
