from Tkinter import *

def iCalc (source, side) :
	storeObj = Frame(source, borderwigth=4, bd=4, bg="grey")
	storeObj.pack(side=side, expand=YES, fill=BOTH)
	return StoreObj

def button(source,side,text, command=None):
	storeObj = Button(source, text=text, command=command)
	storeObj.pack(side=side,expand=YES,fill=BOTH)
	return storeObj

class app (Frame):
	def __init__(self) : 
		Frame.__init__(self)
		self.option_add('*Front', 'arial 20 bold')
		self.pack(expand=YES,fill=BOTH)
		self.master.title('Calculator')

		display = StringVar()
		Entry(self, relief=FLAT, textvariable=display,justify='right',bd=30, bg="grey").pack(side=TOP, expand=YES,fill=BOTH)

		for clearBut in (["CE"],["C"]):
			erase=iCalc(self,TOP)
			for ichar in clearBut:
				button(erase, LEFT, ichar, lambda storeObj=display, q=ichar: storeObj.set(''))

		for Numbut in ("789/","456*","123-","0.+"):
			FunctionNum = iCalc(self, TOP)
			for iEquals in NumBut:
				button(FunctionNum, LEFT, iEquals, lambda storeObj=display,  storeObj.set(storeObj.get() +q))
		EqualsButton = iCalc(self, TOP)
		for iEquals in "=" :
			if iEquals=='=':
				btnEquals = button (EqualsButton, LEFT, iEquals)
				btniEquals.bind('<ButtonRelease-1>',lambda e, s=self,storeObj=display: s.calc(storeObj), '+')
			else:
				btniEquals = button(EqualsButton, LEFT, iEquals, lambda storeObj=display, s=' %s '%iEquals: storeObj.set(storeObj.get()+s))

	def calc(self,display):
		try:
			diplay.set(eval(display.get()))
		except:
			display.set("ERROR")

if __name__ == '__main__':
	app().mainloop()

